def fun(args):
   return isCyclic(args[0]) and isCyclic(args[1]) and args[2] == '{id}'

""" """

def fun(args):
   n=GSubscriptDigits.index(args[0][1])
   m=GSubscriptDigits.index(args[1][1])
   if m%n != 0:
      return 0
   else:
      return totient(n)

"""
ℤ𝘯 ℤ𝑚 {id}

if not n || m , none. if yes, then, it's the number of guys k relatively prime to n; then take the generator to r^km/n


