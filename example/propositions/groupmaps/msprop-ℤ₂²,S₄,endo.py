[['!', 'D₂', 'ℤ₂', 'D₃', 'ℤ₃', 'S₃'], 'S₄', 'endo']
""" """
def fun(args):
   args[2] = 'outer'
   return Args_LookupValue(args)

"""

for n=4, we have an additional normal subgroup, the pairs of transpositions + e. what's the quotient? it's order |S₄| / 4 = 6. gotta be D₆ right? only other possibility is ℤ₆, but nothing in S₄ is order 6.
so the only embeddings in the image of a non-iso endo have to be ℤ₂, ℤ₃, and D₃

»propositions/groupmaps/msprop-X-S𝘯-endo.py»

