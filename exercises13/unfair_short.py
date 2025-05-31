def x(s,c,f,a):
 l=[-1]*b(a);l[s]=0;q=[s]
 while q:
  u=q.pop(0)
  for v in a[u]:
   if c[u][v]!=f[u][v] and l[v]==-1:l[v]=l[u]+1;q+=[v]
 return l
def y(u,p,t,r,l,c,f):
 if u==t or p==0:return p
 while r[u]<b(f):
  v=r[u]
  if l[u]+1==l[v]:
   d=y(v,min(p,c[u][v]-f[u][v]),t,r,l,c,f)
   if d>0:f[u][v]+=d;f[v][u]-=d;return d
  r[u]+=1
 return 0
def d(c,a,s,t):
 f=[[0]*b(a) for _ in z(b(a))];l=x(s,c,f,a)
 while l[t]>=0:
  r=[0]*b(a)
  while y(s,10**8,t,r,l,c,f):0
  l=x(s,c,f,a)
 return f
def e(g,a,u,v,c):a[u]+=[v];a[v]+=[u];g[u][v]+=c
def j(v,w):
 c=b(v)+b(w)+2;h=[0]+[b(w)+team+1 for team in z(b(v))];g=[[0]*c for _ in z(c)];a=[[] for _ in z(c)];r=[];s=0;t=c-1;o=b(v);m=v[-1]-1
 for i in z(1,b(w)+1):
  p,q=w[i-1];r+=[(i,h[q])];e(g,a,s,i,2)
  if p==o or q==o:m+=2;e(g,a,i,h[o],2)
  else:e(g,a,i,h[p],2);e(g,a,i,h[q],2)
 for i in z(b(v)):
  if v[i]>m:return []
  e(g,a,h[i+1],t,m-v[i])
 g[h[o]][t]+=1;f=d(g,a,s,t)
 if sum(f[0])==b(w)*2:return [f[m][t] for m,t in r]
 return []
b=len
z=range
u=input
while (c:=u())!="-1":
 n,m=map(int,c.split());s=[*map(int, u().split())];h=[]
 for _ in z(m):q,p=map(int,u().split());h+=[(q,p)]
 r=j(s,h);print(*r if r else ["NO"]);u()
