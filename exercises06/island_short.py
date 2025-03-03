import math;d=math.dist;e=enumerate;i=input;r=range
for _ in r(int(i())):
 b=[[*map(float,i().split())]for _ in r(int(i()))];c=[d(b[t:=0],p)for p in b]
 for _ in b[1:]:n,k=min([(c,j)for j,c in e(c)if c]);t+=n;c=[min(c[j],d(b[k],p))for j,p in e(b)]
 print(t)