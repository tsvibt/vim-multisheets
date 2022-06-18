def fun(args):
   return args[0] == 'ℤ₂' and isDihedral(args[1])

""" """
def fun(args):
   n=GSubscriptDigits.index(args[1][1])
   if n==2:
         return {'{id}': n+1, 'inner': 3, 'outer': 1, 'endo': 1}[args[2]]
   elif n%2==0:
      if n%4==0:
         return {'{id}': n+1, 'inner': 3, 'outer': 2, 'endo': 1.5}[args[2]]
      else: 
         return {'{id}': n+1, 'inner': 3, 'outer': 2, 'endo': 1}[args[2]]

   else:
      return {'{id}': n, 'inner': 1, 'outer': 1, 'endo': 1}[args[2]]


"""

ℤ₂ D𝘯

any D𝘯 is representable like:
<r,f: rⁿ = f² = 1, fr = r^-1f>
an automorphism has to take r to some rotation (assuming n>2) that generates the rotations, and then has to specify where the f goes; then everything else follows.
and this can be done in any way: for any reflection r^kf and any r^j , we have 
(r^j)^n = r^jn = 1
(r^k f)² = r^k r^-k f² = r^kn 1 = 1
(r^k f) r^j = r^k (r^-1)^j f = r^-j (r^k f)

as long as j ⊥ n, this gives an automorphism, and this clearly covers all automorphisms.

when do these come from conjugation?
conjugating by a flip takes r -> r^-1 and r^k f to fr^kff^-1 = r^-k f
conjugating by a rotation r^j fixes rotations and takes f to r^j f r^-j = r^2j f, generally r^k f to r^(k + 2j) f

so any auto that takes r to something other than r, r^-1, is an outer.
among those that take r to r, r^-1, ....  if r to r, what's left is to specify where f goes. if {r^2j | j in [n]} is all rotations, ie if n is odd, then we have all these. otherwise, we only have half, and the others give outers. 
if r to r^-1, from flip r^k f, then f goes to r^k f f f^-1 r^-k = r^2k f. so again if n is odd, we have all, and if not, the others are outer.

for endo: r^2 must go to either r^2 or 1, as those are the only squares. but f can go to r^2: map r and f to r^2. then 
ϕf ϕr = r^2 r^2 = r^-2 r^2 = ϕr^-1 ϕf, so this is a homomorphism.
not sure how to render this; for now saying 1.5, counting f as a half...
....OOPS. this is wrong... confused r^2 with r^n/2 i guess?
by the analysis in »propositions/groupmaps/msprop-ℤ₂²-D𝘯.py» , if n has exactly 1 factor of 2, then, everything is made equivalent. otherwise, we get 1.5 because we can quotient by ℤ𝘯 and send that to r^n/2


