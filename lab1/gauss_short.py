def g(m,b):
 e=1e-9;a=[m[i]+[b[i]] for i in range(len(b))];n=len(b);w=[-1]*n;r=0
 for c in range(n):
  p=r
  for i in range(r,n):
   if abs(a[i][c])>abs(a[p][c]):p=i
  if abs(a[p][c])<e:continue
  for i in range(c,n+1):a[p][i],a[r][i]=a[r][i],a[p][i]
  w[c]=r
  for i in range(n):
   if i==r:continue
   k=a[i][c]/a[r][c]
   for j in range(c,n+1):a[i][j]-=a[r][j]*k
  r+=1
 l=[0.0]*n
 for i in range(n):
  if w[i]!=-1:l[i]=a[w[i]][n]/a[w[i]][i]
 for i in range(n):
  s=sum([l[j]*a[i][j] for j in range(n)])
  if abs(s-a[i][n])>e:return []
 for i in range(n):
  if w[i]!=-1:continue
  l[i]=float("inf")
  for j in range(n):
   if abs(a[j][i])<e:continue
   l[w.index(j)]=float("inf")
 return l
if __name__=="__main__":
 P=1;o=list();n=0;m=list()
 for l in [[*map(float,x.split(" "))] for x in open(0,"r").read().split("\n")[:-1]]:
  if n==0:m=list();n=int(l[0])+1;continue
  if n==1:
   t=g(m,l)
   if len(t)==0:o.append("inconsistent")
   elif float("inf") in t and not P:o.append("multiple")
   else:o.append(" ".join(list(map(str,map(lambda x:x,t)))).replace("inf","?"))
  else:m.append(l)
  n-=1
 open(1,"w").write("\n".join(o))