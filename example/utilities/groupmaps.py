
from math import gcd, factorial


def totient(n):
   result = 0        
   for k in range(1, n+1):
      if gcd(k, n) == 1:
         result += 1
   return result

GSubscriptDigits = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', ]

def isCyclic(x):
   return len(x) == 2 and x[0] == 'ℤ' and x[1] in GSubscriptDigits

def isDihedral(x):
   return len(x) == 2 and x[0] == 'D' and x[1] in GSubscriptDigits

def isSymmetric(x):
   return len(x) == 2 and x[0] == 'S' and x[1] in GSubscriptDigits


