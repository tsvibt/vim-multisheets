def fun(args):
   if args[2] == 'outer':
      return args[1] in Instances('GroupNoOuters') 
   else:
      return False

"""
"""
def fun(args):
   args[2] = 'inner'
   return Args_LookupValue(args)


"""

no extra outer automorphisms

