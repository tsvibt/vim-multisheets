def fun(args):
   if args[2] == 'endo':
      args[2] = 'outer'
      return Args_LookupValue(args) in ['0', '1']
   else:
      return False

"""
"""
def fun(args):
   args[2] = 'outer'
   return Args_LookupValue(args)


"""

outer empty or single
