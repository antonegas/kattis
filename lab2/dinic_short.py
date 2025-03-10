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
i=input;p=print;b=len;z=range
n,m,s,t=map(int,i().split())
c=[[0]*n for _ in z(n)]
a=[[] for _ in z(n)]
e=[]
for _ in z(m):
 u,v,k=map(int,i().split())
 if c[u][v]+c[v][u]==0:a[u]+=[v];a[v]+=[u]
 if c[u][v]==0:e+=[(u, v)]
 c[u][v]+=k
f=[[0]*b(a) for _ in z(b(a))];l=x(s,c,f,a)
while l[t]>=0:
 r=[0]*b(a)
 while y(s,10**8,t,r,l,c,f):0
 l=x(s,c,f,a)
m=sum(f[s])
e=[(u,v,f[u][v]) for u,v in e if f[u][v]>0]
p(n,m,b(e))
for u,v,f in e:p(u,v,f)