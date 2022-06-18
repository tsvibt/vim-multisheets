def fun(args):
   if args[2] == 'inner':
      args[2] = '{id}'
      return Args_LookupValue(args) in ['0', '1']
   else:
      return False

""" """
def fun(args):
   args[2] = '{id}'
   return Args_LookupValue(args)


"""
id empty or single



