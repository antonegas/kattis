from functools import *
from math import log2 as l
r=reversed
def f(t):
 c=1
 for i,x in r([*enumerate(t)]):
  if c*l(x)>1024:
   if i==0:return [],1,c*l(x)
   return t[:i],i+1,c*l(x)+l(l(t[i-1]))
  c=x**c
 return [],0,c
def g(a,b):
 a1,a2,a3=a;b1,b2,b3=b
 if a2>b2:return 1
 if b2>a2:return -1
 if a3>b3:return 1
 if b3>a3:return -1
 for a4,b4 in r([*zip(a1,b1)]):
  if a4>b4:return 1
  if b4>a4:return -1
 return 0
print("Case 1:")
n=int(input())
i=[input() for _ in range(n)]
t=[list(map(int,s.split("^"))) for s in i]
v=[]
for j in t:
 if 1 in j:j=j[:j.index(1)]
 v.append(f(j))
for j in sorted(range(n),key=cmp_to_key(lambda a,b:g(v[a],v[b]))):print(i[j])
