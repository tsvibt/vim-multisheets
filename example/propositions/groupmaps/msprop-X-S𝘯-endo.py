def fun(args):
   return isSymmetric(args[1]) and args[2] == 'endo' and GSubscriptDigits.index(args[1][1]) != 4 and args[0] not in ['â¤â', 'Dâ']
""" """
def fun(args):
#   n=GSubscriptDigits.index(args[1][1])
   args[2] = 'outer'
   return Args_LookupValue(args)

"""

X Sğ¯ endo
endo. for n>4, Sğ¯ has only Ağ¯ as a normal subgroup, i.e. its image is â¤â, which doesn't support any other embeddings. 
for n=4, we have an additional normal subgroup, the pairs of transpositions + e. what's the quotient? it's order |Sâ| / 4 = 6. gotta be Dâ right? only other possibility is â¤â, but nothing in Sâ is order 6.




