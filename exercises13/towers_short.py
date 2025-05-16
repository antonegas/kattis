from functools import *
from math import log2 as l
p=print
h=input
m=range
def f(s):
 c=1;t=[*map(int,s.split("^"))]
 if 1 in t:t=t[:t.index(1)]
 while t:
  if c*l(x:=t.pop())>1024:return t,len(t)+1,c*l(x)+l(l(t[-1]))*(len(t)>0)
  c=x**c
 return [],0,c
def g(a,b):
 a=f(a);b=f(b)
 if (y:=a[1:])!=(v:=b[1:]):return (-1)**(y<v)
 for c,d in [*zip(a[0],b[0])][::-1]:
  if c-d:return c-d
 return 0
for j in ["Case 1:"]+sorted([h() for _ in m(int(h()))],key=cmp_to_key(g)):p(j)