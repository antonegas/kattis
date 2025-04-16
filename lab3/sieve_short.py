b=lambda a,i:1-bool(a[i//8]&(1<<(i%8)))
r=range
n,q=map(int,input().split())
a=bytearray(n//8+1)
c=0
a[0]=3
for i in r(2,n+1):
 if b(a,i):
  c+=1
  for j in r(i**2,n+1,i):a[j//8]|=1<<(j%8)
print(c)
for _ in r(q):print(b(a,int(input())))