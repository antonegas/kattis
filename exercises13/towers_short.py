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
 x,y,z=a;u,v,w=b
 if y>v:return 1
 if v>y:return -1
 if z>w:return 1
 if w>z:return -1
 for c,d in r([*zip(x,u)]):
  if c>d:return 1
  if d>c:return -1
 return 0
p=print
h=input
m=range
p("Case 1:")
n=int(h())
i=[h() for _ in m(n)]
t=[[*map(int,s.split("^"))] for s in i]
v=[]
for j in t:
 if 1 in j:j=j[:j.index(1)]
 v.append(f(j))
for j in sorted(m(n),key=cmp_to_key(lambda a,b:g(v[a],v[b]))):p(i[j])
