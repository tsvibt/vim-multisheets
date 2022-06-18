def fun(args):
   return args[0] == 'ℤ₂²' and isDihedral(args[1]) 

""" """
def fun(args):
   n=GSubscriptDigits.index(args[1][1])
   if n==2:
      return {'{id}': 3*n, 'inner': 6, 'outer': 1, 'endo': 1}[args[2]]
   elif n%2==0:
      if n%4==0:
         return {'{id}': 3*n, 'inner': 6, 'outer': 3, 'endo': 3}[args[2]]
      else: 
         return {'{id}': 3*n, 'inner': 6, 'outer': 3, 'endo': 1}[args[2]]
   else:
      return {'{id}': 0, 'inner': 0, 'outer': 0, 'endo': 0}[args[2]]


"""

ℤ₂² D𝘯

if n odd, composing distinct reflections gives a rotation, not order 2, so there's no maps.

if n even, then, for any f, we have {f, r^n/2 f , r^n/2, e} ≅ ℤ₂² (as r^n/2 f = r^-n/2 f = f r^n/2)
given a pair (f, r^n/2 f), the two generators can go to anyof the 3 elements of the grp , so we have  6x number of pairs ; there are n reflections, so n/2 pairs. that's all the maps: there's only 1 rotation order 2, so the image has two reflections, which must multiply to an order 2 rotation.

automorphisms:
rotation is fixed, so f's image determines the map. where can f be taken? say for some j, reflection g = r^k f has 
g r^n/2 f g^-1 = r^j f. then 
r^k f r^n/2 f f r^-k = r^j f
r^k  r^-n/2 r^k f = r^j f
2k-n/2=j
k=(j+n/2)/2
this is possible exactly when j+n/2 is even, i.e. for half of j in [n]. so we divide the number of maps by n/2, giving 6.
what are the six maps? it depends: if 4 || n, there's 3 maps onto {f, r^n/2 f, r^n/2, e}, and three into {r f, r^1+n/2 f, r^n/2, e}, where sending the generators to the two reflections is equivalent either way; otherwise , f and r^n/2 f are not conjugate, and the maps are the six maps onto {f, r^n/2 f, r^n/2, e}.

including outers, f can be taken anywhere. so the choice is just, both generators to reflections, or one or the other to r^n/2. for D₂, these aren't different, because r^n/2 can also be moved around.

endos. what are the normal subgroups of D₂𝘯? ℤ𝘯 is one, with quotient ℤ₂. others? if only reflections, then, it's a single reflection (composing two different reflections gives a rotation). is that normal? no (except for D₂): rfr^-1 = r^2f ≠ f 
if it includes a rotation r^k, it includes r^j f r^k f r^-j = r^-k. this is sufficient and satisfied by any subgroup of ℤ𝘯. 
can there also be a reflection? say we have f and r^k (k minimum in the group). we also have r^jk. and r f r^-1 = r^2 f. so we also have r^2 f f = r^2. thus k=2. instead of f we could have r f, but that's it. 
so we have 
ℤ𝑚 for m | n
<f, r^2>
<rf, r^2>
quotients? quotienting by anything that contains r^n/2 will kill homs from ℤ₂², since those have to include r^n/2. we avoid r^n/2 iff m is odd, i.e. if ℤ𝑚 = {r^(j2^k)} where j is anything and k is maximal s.t. 2^k | n

... anyway, the question is, can we take a reflection to r^n/2, or vice versa? actually these are the same question since if we have ℤ₂²  E->  D𝘯   F->  D𝘯, and E;F is an embedding, then either Fr^n/2 = r^n/2, or else Fr^n/2 is a flip, and some flip f has Ff = r^n/2.
we're talking about D𝘯 = D₂𝑚. what's D₂𝑚 / ℤ𝑚? it's ℤ₂², but it kills r^n/2. 
D𝘯 / <f, r^2> = D𝘯 / <rf, r^2> = ℤ₂, so these can't map a ℤ₂² embedding
we have to not kill r^n/2. so we have to choose... 
what's D𝘯 / ℤ𝑚? i think it's D(n/m). 
we have (ϕr)^n/m = 1, (ϕf)^2 = 1, and ϕrϕf = ϕrf = ϕfr^-1 = ϕfϕr^-1. why aren't there other relations? this already gives the correct order.
given D𝘯 / ℤ𝑚 = D(n/m) = <r', f', ....> , if n/m is odd, then m was even and we killed r^n/2. otherwise, if n/m > 2, then r'^n/2m is a nontrivial power of r', so it must be sent to r^n/2 ∈ D𝘯. this doesn't help. 
the remaining case though, where m is odd and n/m=2, we have D(n/m) = D₂ = ℤ₂². in this case, the endomorphism can take an image of D₂ to any image of D₂. this makes all embeddings equivalent.
so if n/2 is odd, we get 1; otherwise , we get 3. 






