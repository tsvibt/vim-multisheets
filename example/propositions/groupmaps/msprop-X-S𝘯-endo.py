def fun(args):
   return isSymmetric(args[1]) and args[2] == 'endo' and GSubscriptDigits.index(args[1][1]) != 4 and args[0] not in ['ℤ₂', 'D₂']
""" """
def fun(args):
#   n=GSubscriptDigits.index(args[1][1])
   args[2] = 'outer'
   return Args_LookupValue(args)

"""

X S𝘯 endo
endo. for n>4, S𝘯 has only A𝘯 as a normal subgroup, i.e. its image is ℤ₂, which doesn't support any other embeddings. 
for n=4, we have an additional normal subgroup, the pairs of transpositions + e. what's the quotient? it's order |S₄| / 4 = 6. gotta be D₆ right? only other possibility is ℤ₆, but nothing in S₄ is order 6.




