def fun(args):
   return args[0] == 'ℤ₂' and args[1][0] == 'S' and args[1][1] in GSubscriptDigits and not (GSubscriptDigits.index(args[1][1]) == 6 and args[2] in ['outer', 'endo'])

""" """
def fun(args):
   n=GSubscriptDigits.index(args[1][1])
   count = 0
   for i in range(n//2):
      k=i+1
      count+= int(factorial(n) / ((2**k)*factorial(k)*factorial(n-2*k))) 
   if n in [3]:
      endo = 1
   else: 
      endo = n//4 + (n//2 - n//4)/(1+(n//4))
   endo = round(endo, 2)
   return {'{id}': count, 'inner': n//2, 'outer': n//2, 'endo': endo}[args[2]]



"""
ℤ₂,S𝘯 not S₆

count elements of order 2
(12) has (n 2)/(n-2)!
(12)(34) has n!/2*2*2*(n-4)! 

in general to have k pairs, there's n!/(2^k*k!*(n-2k)!) because we take any permutation, and pair off the first k pairs; swapping within a pair (2^k), permuting the pairs (k!), and permuting the unpaired elements ((n-2k)!), doesn't make a difference.

inner autos are conjugations, ie relabelings of the acted set, which can change to any element with same cycle structure. so we just have the max number of pairs n//2. except for S₆ there are no outers.

endo. for n>4, S𝘯 has only A𝘯 as a normal subgroup, i.e. its non-iso endos are maps that kill all even cycles and take all odd cycles to some involution. for n=6, this means we can't take (12)(34) to (12), but we can vice versa, giving 1.5
for n=5 or n>6, all the even involutions have their own class, but all the odds can be taken to any even.... don't know how to render this! i guess divide them by how many they go to...? there's n//4 even involutions, n//2 - n//4 odd involutions, each odd goes to itself or some even.

for n=4, as above we can send odd to even. can we send even to odd? we have an additional normal subgroup, the pairs of transpositions + e. but that's the even ones; so quotienting kills the evens and can't send one to an odd.

3   , 9   , 25  , 75  , 231 , 763 , 2619
https://oeis.org/A001189

