def fun(args):
   return isCyclic(args[0]) and isDihedral(args[1]) and GSubscriptDigits.index(args[0][1]) > 2
""" """
def fun(args):
   n=GSubscriptDigits.index(args[0][1])
   if GSubscriptDigits.index(args[1][1]) % n != 0:
      return 0
   else:
      Zautos = totient(n)
      return {'{id}': Zautos, 'inner': int(Zautos / 2), 'outer': '??', 'endo': '??'}[args[2]]

"""

Z𝑚 D𝘯

if the order of the cyclic subgroup, m, is not divisible by n, there are no elements of order n, hence no embeddings of ℤ𝘯, unless n=2 (giving embeddings to the flips)

if it is, then there's exactly one subgroup ℤ𝘯. any embedding ℤ𝘯 -> ℤ𝘯 works.
conjugating by r^k does nothing. conjugating by f takes r^k -> r^-k, which pairs off possible images of the generator of ℤ𝘯, dividing by two (r^n/2 can't be an image of the generator since n>2)
allowing all automorphisms...

