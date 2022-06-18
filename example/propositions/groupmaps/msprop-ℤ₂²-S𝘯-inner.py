def fun(args):
   return args[0] == 'ℤ₂²' and isSymmetric(args[1]) and args[2] == 'inner'
""" """
def fun(args):
   n=GSubscriptDigits.index(args[1][1])
   count = 0
   for b in range((n//4) + 1):
      for i in range((n//2) + 1):
         for j in range((n//2) + 1):
            for k in range((n//2) + 1):
               if 2*(2*b+i+j+k) < n+1 and (b>0 or sum([1 if x>0 else 0 for x in [i,j,k]]) > 1):
                  count += 1
   return int(count)

"""

ℤ₂² S𝘯 inner

... wait no. we have... wait...
if you have the same ABC type, then you are conjugate.
what if you have different ABC type?
could be like 2,3,4 vs 2,4,3. so... those subgroups are conjugate.... but the composite embedding is still different, the image of 2+3 will not be taken to the image of 2+4
one of the sums changes, so it's different

0 3 3 10 10 22 22
not in oeis
0 , 4 , 4 , 14, 14, 33, 33,

def fun(n):
   count = 0
   for b in range((n//4) + 1):
      for i in range((n//2) + 1):
         for j in range((n//2) + 1):
            for k in range((n//2) + 1):
               if 2*(2*b+i+j+k) < n+1 and (b>0 or sum([1 if x>0 else 0 for x in [i,j,k]]) > 1):
                  code = [2*b, i , j, k]
                  print(code)
                  z=0
                  s =''.join([str(x) for x in range(n)])
                  for x in [2*b, i , j, k]:
                     zzz = ''
                     for q,w in enumerate(s[z:z+2*x]):
                        if q%2==0:
                           zzz += '(' + w + s[z:z+2*x][q+1] + ')'
                     print('[' + zzz + ']', end='')
                     z+=2*x
                  print('')



