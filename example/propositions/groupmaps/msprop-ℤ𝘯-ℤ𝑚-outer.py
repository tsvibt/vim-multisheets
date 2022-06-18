def fun(args):
   return isCyclic(args[0]) and isCyclic(args[1]) and args[2] == 'outer'

"""
"""

def fun(args):
   n=GSubscriptDigits.index(args[0][1])
   m=GSubscriptDigits.index(args[1][1])
   if m%n != 0:
      return 0
   else:
      return 1


"""



ℤ𝘯 ℤ𝑚 outer

if n || m , tn=totient(n). then take the generator to r^km/n, k ⊥ n. the autos are sending r to r^j for some j ⊥ m. this sends
r^km/n to r^jkm/n 
now since j ⊥ m and n || m, also j ⊥ n; so we've gotten another generator. 
have k, i ⊥ n. can r^km/n be taken to r^im/n?
i.e. does r^im/n = r^jkm/n  for some j ⊥ m?
since r^km/n generates {r^m/n}, for some j, r^im/n = r^jkm/n  
is this j ⊥ m?
we also have j+qn for any q. is one of them ⊥ m?
if x ⊥ n and x ⊥ m/n, then x ⊥ m
j+qn ⊥ n since j ⊥ n, since r^i also generates {r^k}, so that i ⊥ n, where i≡jk mod n
can j+qn be ⊥ m/n?
if j+qn not ⊥ m/n, that's because it shares a factor f with m that isn't a factor of n. but if it isn't a factor of n, then adding n will make it not a factor. 
so either j or j+n ⊥ m? no we could get a new factor
eg m=30 n=5 j=3, j+n=8
let n' be Πp^(m_p) for p prime factor of n, m_p maximal p^m_p || m
j ⊥ n'
n ⊥ m/n'
so n mod m/n' generates [m/n']
so ng = j mod m/n' for some g
so j+ng 


starting over, ok so... assuming n || m:
let m' = m/n, take any j ⊥ n. 
we want to construct an automorphism of ℤ𝑚 that takes r^m' to r^jm'
automorphisms are of the form r^i -> r^ik, where k is fixed and ⊥ m.
so we want some k ⊥ m s.t. r^km' = r^jm' 
i.e., km' = jm' mod m, which holds when k = j + gn, some g. 

let n' be Πp^(m_p) for p prime factor of n, m_p maximal s.t. p^m_p || m

n ⊥ m/n'
so n mod m/n' generates [m/n']

want j+gn ⊥ m
have j+gn ⊥ n' (a shared prime would be in n, so must also be in j, contradicting j ⊥ n)
suffices: j+gn ⊥ m/n' since n' * m/n' = m
suffices: j+gn = 1 mod m/n'

since n mod m/n' generates [m/n'], 
ng = j + 1 mod m/n' for some g

so j+ng  is the desired k. so the automorphism exists and all maps are equivalent.

