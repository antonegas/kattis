from math import acos,pi
def i(p, vs):
 x,y=p;s=0
 for u,v in zip(vs,vs[1:]+[vs[0]]):
  x1,y1=u;x2,y2=v;x1-=x;x2-=x;y1-=y;y2-=y
  if x1==0 and y1==0:return 0
  if x2==0 and y2==0:return 0
  r=(x1*x2+y1*y2)/(sq(x1,y1)*sq(x2,y2))
  if r>1:r=1
  if r<-1:r=-1
  a=acos(r)
  if x1*y2-x2*y1>0:a=-a
  if abs(a-pi)<1e-7:return 0
  s+=a
 if abs(s)>pi:return 1
 return -1
f=lambda:[*map(int,input().split())]
sq=lambda x,y:(x*x+y*y)**0.5
while n:=int(input()):
 vs=[f() for _ in range(n)]
 for _ in range(int(input())):
  r=i(f(),vs)
  if r>0:print("in")
  elif r<0:print("out")
  else:print("on")