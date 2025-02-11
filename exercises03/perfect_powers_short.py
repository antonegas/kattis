for n in map(int,open(0).read().split()[:-1]):
 for b in range(2,int(pow(n,0.5))+1):
  x=abs(n);p=0
  while x%b==0:x//=b;p+=1
  if (x==1)&((n>0)|(p%2)):print(p);break
 else:print(1)