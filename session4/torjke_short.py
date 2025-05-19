from math import comb
def t(p):
 c=0
 for i in range(len(p)):
  x,y=p[i];l={}
  for j in range(i+1,len(p)):
   a,b=p[j];k=999
   if x<a:k=(b-y)/(a-x)
   elif x>a:k=(y-b)/(x-a)
   if k in l:l[k]+=1
   else:l[k]=1
  for q in l:c+=comb(l[q], 2)
 return c
n=int(input())
p=[]
for y in range(n):p+=[(x,y) for x, l in enumerate(input()) if l!="."]
print(t(p))