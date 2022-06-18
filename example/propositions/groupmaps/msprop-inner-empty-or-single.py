def fun(args):
   if args[2] == 'outer':
      args[2] = 'inner'
      return Args_LookupValue(args) in ['0', '1']
   else:
      return False

"""
"""
def fun(args):
   args[2] = 'inner'
   return Args_LookupValue(args)


"""

inner empty or single
