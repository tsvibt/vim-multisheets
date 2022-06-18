def fun(args):
   return args[2] == 'inner' and args[1] in Instances('AbelianGroup')
"""
"""
def fun(args):
   args[2] = '{id}'
   return Args_LookupValue(args)
"""
if the target is abelian, conjugation doesn't do anything, so there's only the trivial inner automorphism, and no embeddings are made equivalent.



