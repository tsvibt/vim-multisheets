python3 << endpython3
import vim

#Copyright 2022 Tsvi Benson-Tilsen
#Licensed under the GNU General Public License. See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

from os import path, rename, listdir, remove
import fileinput
import re
import time
from collections import deque
from functools import reduce
import pprint
pp = pprint.PrettyPrinter()
import copy
import ast
# this order necessary to set flag
import tabulate
tabulate.PRESERVE_WHITESPACE = True
from tabulate import tabulate

### function definition files
Fdefpre = "ms-"
def Fdeffile_Fname(fn):
   return fn[len(Fdefpre):]

def Fname_Fdeffile(fn):
   return Fdefpre + fn

def isFdeffile(file):
   return file.startswith(Fdefpre)

### proposition files
#Propdir = "propositions/"
Propdir = vim.eval('g:multisheets_propdir') 
Propnamepre = "msprop-" 
def Fname_Proppre(funcname):
   return  Propdir + funcname + "/" + Propnamepre

def Fname_Propname_Propfile(funcname, propname):
   return Fname_Proppre(funcname) + propname + ".py"

def Propfile_Fname(file):
   return file.split('/')[1]

def isPropfile(file):
   return file.startswith(Propdir) and ((file.split('/'))[-1]).startswith(Propnamepre)

### sheet files
Msheetdir = "sheets/"
def Fname_FsheetF(fn):
   return Msheetdir + fn

def Fsheetfile_Fname(fn):
   return fn[len(Msheetdir):]

def isFsheetfile(file):
   return file.startswith(Msheetdir)

### type definition files
Typepre = "type-"
def Type_Tfile(tp):
   return Typepre + tp


def vim_Maybe_File_Fsheet(file):
   if isFsheetfile(file):
      return vim_File_Fsheet(file)
   return file

# main thing: recompute the sheet and return its location
def vim_File_Fsheet(file):
   if isFdeffile(file):
      funcname = Fdeffile_Fname(file)
      file = Fname_FsheetF(funcname)
   if isFsheetfile(file):
      if not path.exists(Msheetdir):
         TouchDirectory(Msheetdir)
      utilitiesfile = 'utilities/' + Fsheetfile_Fname(file)+ '.py'
      if not path.exists(utilitiesfile):
         TouchDirectory('utilities/')
         TouchFile(utilitiesfile)
      if not path.exists(Propdir):
         TouchDirectory(Propdir + funcname)
      utilities = Read(utilitiesfile)
      exec(utilities if utilities!=None else '', globals())
      do_FsheetF_UpdateFsheet(file)
      return file
   return file

def do_FsheetF_UpdateFsheet(file):
   TouchFile(file)
   TF_Write(Text_FsheetF_Fsheet(CacheRead(file), file), file)

def Fname_Fdata(funcname):
   funclines = CacheRead(Fname_Fdeffile(funcname)).split('\n')
   argtypes = CleanTokens(funclines[1])
   argtypeinsts = [{'type': t, 'instances': Instances(t)} for t in argtypes]
   if funclines[0]!='':
      argnames = CleanTokens(funclines[0])
      for i in range(len(argnames)):
         if not i<len(argtypes):
            argnames.append("v" + str(i))
   else:
      argnames = argtypes
   return {'argnames': argnames, 'argtypes': argtypes,}

def Text_FsheetF_Fsheet(fsheet, file):
   funcname = Fsheetfile_Fname(file)
   fdata = Fname_Fdata(funcname)
   line0 = [funcname + ': '] + fdata['argnames']
   line1 = ['types: '] + fdata['argtypes']
   lines = fsheet.split('\n')
   if len(lines)>3:
      args = CleanTokens(lines[2])[1:]
      line2 = ['values: '] + args
      message,axes,sheet= Fname_Args_MessageAxesSheet(funcname, args)
   else:
      line2 = ['values: '] + [Instances(argtype)[0] for argtype in fdata['argtypes']]
      message,axes,sheet= 'message: init', '', ''
   table0 = tabulate([line0, line1, line2], tablefmt='plain')
   #warning: the parsing in other functions relies on this formating
   return '\n'.join([table0, '', message, axes, sheet])

def Fname_Args_MessageAxesSheet(funcname, args):
   global GReadCache
   global GUseReadCache
   GUseReadCache=True
   GReadCache={}
   fdata = Fname_Fdata(funcname)
   if args.count('X') != 1 or args.count('Y') != 1:
      result = ('message: there should be one X coordinate and one Y coordinate, got ' +str(args), '', '')
   else:
      starttime = time.time()
      indexX = args.index('X')
      typeX = Instances(fdata['argtypes'][indexX])
      indexY = args.index('Y')
      typeY = Instances(fdata['argtypes'][indexY])
      propositions = Fname_Theorems(funcname)
      arginstance = copy.copy(args)
      ll = [[x] + [Props_Args_Conclusion(propositions, replace(replace(arginstance, indexX, x), indexY, y))['value'] 
            for y in typeY] for x in typeX]
##    profiling.  need this, not the list comp, maybe because https://github.com/inducer/pudb/issues/103
#      cmd = """for x in typeX:
#   for y in typeY:
#      Props_Args_Conclusion(propositions, replace(replace(arginstance, indexX, x), indexY, y))['value']
#      """
#      PROF(cmd, locals())
      

   #   wcols = 80
      wcols = int(vim.eval('winwidth(0)')) -3 -2 
      maxlen = max([len(f) for f in typeX + typeY] + [max([len(val) for val in l]) for l in ll])
      colwidth = min(maxlen, (wcols // (len(typeY)+1)) -3)

      ll.insert(0, ['X' + ' '*(colwidth - 2) +'Y'] + typeY)
      lines = [[x.strip(' ')[:colwidth].ljust(colwidth) for x in line] for line in ll]
      table = tabulate(lines, headers='firstrow', tablefmt='pretty')
      axesnames = "X: " + fdata['argnames'][indexX] + "    Y: " + fdata['argnames'][indexY]
      endtime = time.time()
      result = ('message: updated ' + GetTimestamp().split('-')[-1].split('.')[0] 
               + ', computing sheet took ' + str(endtime - starttime )[:6] + ' seconds', axesnames, table)

   GUseReadCache=False
   return result

GProfileFile ='__cProfileLOG' 
def PROF(cmd, localvars):
   cProfile.runctx(cmd, globals(), localvars, GProfileFile)
   with open("cProfile_pstats_readable.txt", "w") as f:
       ps = pstats.Stats(GProfileFile, stream=f)
       ps.sort_stats('tottime')
       ps.print_stats()

def replace(xs, index, x):
   xs[index] = x
   return xs

def CleanTokens(line, delim=' '):
   return [i.strip(' ') for i in line.split(delim) if i.strip(' ') != '']

def ComLines(t):
   return [i[2:].strip(' ') for i in t.split('\n') if len(i)>1 and i[:2]=='. ']

def Instances(tp):
   tfile = Type_Tfile(tp)
   if not path.exists(tfile):
      TouchFile(tfile)
   insts = NoDups([i for i in ComLines(CacheRead(tfile))if i != '' and i!= 'X'])
   return ['X'] if insts==[] else insts

def vim_File_Word_Line_Files(args):
   file, word, line, col = args
   line, col = int(line)-1, int(col)
   if isFdeffile(file):
      if line == 1:
         return [Type_Tfile(word)]
   if isFsheetfile(file):
      if line == 0:
         if word == Fsheetfile_Fname(file):
            return [Fname_Fdeffile(word)]
      if line == 1:
         if word == Read(file).split('\n')[1].split(':')[0]:
            return []
         return [Type_Tfile(word)]
      if line > 8:
         funcname, fdata, args = Fsheet_PointInfo(file, line, col)
         if funcname == None:
            return []
         filenames = Props_Args_Conclusion(Fname_Theorems(funcname), args)['sources']
         if filenames == []:
            filename = Fname_Args_Propfile(funcname, args)
            if not path.exists(filename):
               TouchDirectory('/'.join(filename.split('/')[:-1]))
               TF_Write(str(args) + '\n"""\n', filename)
            filenames = [filename]
         return filenames
   return []

def Fname_Args_Propfile(funcname, args):
   return Fname_Propname_Propfile(funcname, ','.join(args))

def Fsheet_PointInfo(file, line, charactercol):
   ll = CacheRead(file).split('\n')
   if line > len(ll)-2:
      return (None, None, None)
   colwidth = len(ll[line].split('|')[1]) + 1
   columnnum = (charactercol // colwidth) -1
   if columnnum == -1:
      return (None, None, None)
   args = CleanTokens(ll[2])[1:]
   funcname = Fsheetfile_Fname(file)
   fdata = Fname_Fdata(funcname)
   for i,x in enumerate(args):
      if x=='X':
         args[i] = Instances(fdata['argtypes'][i])[line-9]
      if x=='Y':
         args[i] = Instances(fdata['argtypes'][i])[columnnum]
   return (funcname, fdata, args)

def Props_Args_Conclusion(propositions, args):
   results = []
   sources = []
   for prop in propositions:
      if prop['conclusion'] != '' and any([MatchCond(propositions, args, cond) for cond in prop['conds']]):
         result = prop['conclusion']
         if type(result) == type(lambda: ()):
            try:
               result = str(result(propositions, copy.copy(args)))
            except:
               raise Exception('function application failed: ' + str(prop['propfile']))
         if result not in ['', '??']:
            results.append(result)
            sources.append(prop['propfile'])
   value = '??' if results == [] else ( '>X<' if len(set(results))>1 else results[0] )
   return {'value': value, 'sources': sources}

def MatchCond(propositions, args, cond):
   if type(cond) == type(lambda: ()):
      return cond(propositions, copy.copy(args)) == True
   else:
      matches = True
      for i,arg in enumerate(args):
         ci = cond[i] 
         if ci[0] == '!':
            if any([arg == tok.strip(' ') for tok in ci[1:]]):
               matches = False
         elif arg != ci and ci not in ['X', 'Y'] and (type(ci) != type([]) or arg not in ci):
            matches = False
      return matches

def Fname_Theorems(funcname):
   propfiles = Sys(['ls ' + Fname_Proppre(funcname) + '*']).split('\n')
   propfiles.sort()
   props = [ParseProp(r) for r in propfiles if r!='']
   return [r for r in props if r!=None]

def Args_LookupValue(propositions, args):
   return Props_Args_Conclusion(propositions, args)['value']

GpropID=0
def PythonCode_FunctionObject(code):
   global GpropID
   GpropID += 1
   code=code.strip('\n')
   name = code.split('(')[0].split(' ')[-1] 
   codelines = code.split('\n')
   argsname = codelines[0].split('(')[1].split(')')[0]
# improve performance by passing propositions, avoiding reparsing them every time Args_LookupValue is evaluated
# rename functions to avoid collisions
   codelines[0] = codelines[0].replace(name + '(', name + str(GpropID) + '(PROPOSITIONS_META, ')
   code = '\n'.join(codelines)
   code = code.replace('Args_LookupValue(', 'Args_LookupValue(PROPOSITIONS_META, ') 
   # put function in global namespace
   exec(code)
   return eval(name + str(GpropID))


def ParseProp(propfile):
   ll = CacheRead(propfile).split('"""')
   if len(ll)>1:
      l0 = ll[0]
      if l0.startswith('def '):
         conds = [PythonCode_FunctionObject(l0)]
      else: 
         conds = [ast.literal_eval(c) for c in CleanTokens(l0, delim='\n')]
      conc = '' if len(ComLines(ll[-1])) == 0 else ComLines(ll[-1])[-1]
      if len(ll)>2:
         conc = PythonCode_FunctionObject(ll[-2])
      return {'propfile': propfile, 'conds': conds, 'conclusion': conc}
   else:
      return None

wordstart = re.compile(' \S')
def vim_CycleArg(vim_args):
   file, n, col, line  = vim_args
   n, col, line = int(n), int(col)-1, int(line)-1
   if isFsheetfile(file):
      ll = CacheRead(file).split('\n')
      starts = list(wordstart.finditer(ll[2]))
      index = 0
      for i, m in enumerate(starts):
         if i == len(starts)-1:
            index = i
         else:
            if m.start()+2+ (starts[i+1].start() -m.start())/2  >col:
               index = i
               break
      types = CleanTokens(ll[1])[1:]
      args = CleanTokens(ll[2])[1:]
      instances = ['X', 'Y'] + Instances(types[index])
      if n >0:
         args[index] = Successor(args[index], instances)
      if n <0:
         args[index] = Predecessor(args[index], instances)
      text = '\n'.join(replace(ll, 2, 'values: ' + ' '.join(args)))
      TF_Write(text, file)
      do_FsheetF_UpdateFsheet(file)
      return min(col, starts[-1].start())
   else:
      return col

def vim_CycleProp(args):
   file, n = args
   n = int(n)
   if isPropfile(file):
      directory = '/'.join(file.split('/')[:-1])
      files = [directory + '/' + f for f in listdir(directory)]
      files = sorted([f for f in files if isPropfile(f)])
      if n >0:
         return Successor(file, files)
      if n <0:
         return Predecessor(file, files)
   else:
      return file

def vim_MaybeRenameFile(args):
   file, lnum = args
   lnum = int(lnum)-1
   if isPropfile(file):
      line=CacheRead(file).split('\n')[lnum].replace(' ', '-')
      if line != '':
         targetfile = Fname_Propname_Propfile(Propfile_Fname(file), line)
         if not path.exists(targetfile):
            rename(file, targetfile)
            return targetfile

def vimDELETE_Prop(file):
   remove(file)


endpython3
