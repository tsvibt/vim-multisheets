python3 << endpython3
import vim

#Copyright 2022 Tsvi Benson-Tilsen
#Licensed under the GNU General Public License. See LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt

from pathlib import Path
import re 
import subprocess
import time
import datetime


def TouchDirectory(dir):
    Path(dir).mkdir(parents=True, exist_ok=True)

def VimPython():
    fun = vim.eval('a:fun')
    args = vim.eval('a:args')
    function = eval(fun)
    # we want to let python funs have no args, so only pass non-empty args
    if isinstance(args, list):
        if len(args)==0:
            returnval = function()
        else:
            returnval = function(args)
    else:
            returnval = function(args)
    if isinstance(returnval, list):
        vim.command("let g:ms_python_returnval= " + str(returnval))
    else:
        vim.command("let g:ms_python_returnval= '" + escapetext(str(returnval)) + "'")

def Read(file):
    with open(file, 'r') as f:
        t = f.read()
    return t

GReadCache={}
GUseReadCache=False

def CacheRead(file):
   global GReadCache
   if GUseReadCache:
      if file not in GReadCache:
         GReadCache[file] = Read(file)
      return GReadCache[file]
   else:
      return Read(file)

def TouchFile(file):
    Path(file).touch()

def TF_Write(text, file):
    with open(file, 'w') as f:
         f.write(text)

def NoDups(ll):
  return list(dict.fromkeys(ll))

def escapetext(s):
	return re.sub(r"\'","''", s)

def Successor(x, ll):
    ll = NoDups(ll)
    if not x in ll:
        return ll[0]
    i = ll.index(x)
    if i == len(ll)-1:
        return ll[0]
    return ll[i+1]

def Predecessor(x, ll):
    ll = NoDups(ll)
    last = len(ll)-1
    if not x in ll:
        return ll[last]
    i = ll.index(x)
    if i == 0:
        return ll[last]
    return ll[i-1]

def Sys(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')

def GetTimestamp():
    CurrentDT = datetime.datetime.now()
    time = CurrentDT.strftime("%y.%m.%d-%H:%M:%S")
    return time + "." + Milliseconds()

def Milliseconds():
    millis = str(int(round(time.time() * 1000000)))
    return millis[-6:]


endpython3

