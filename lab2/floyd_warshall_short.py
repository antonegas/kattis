def fw(g,n):
 for k in n:
  for i in n:
   for j in n:g[i][j]=min(g[i][j],g[i][k]+g[k][j]);g[i][j]=-f if g[i][j]>g[i][k]+g[k][j] else g[i][j]
 return g
p=print
r=range
s=input
f=float("inf")
while 1:
 n,m,q=map(int,s().split())
 if n==m==q==0:break
 ng=r(n)
 g=[[f]*n for _ in ng]
 for u in ng:g[u][u]=0
 for _ in r(m):u,v,w=map(int,s().split());g[u][v]=min(g[u][v],w)
 sp=fw(g,ng)
 for _ in r(q):
  u,v=map(int,s().split());qr=sp[u][v]
  if qr==f:p("Impossible")
  elif qr==-f:p("-Infinity")
  else:p(qr)