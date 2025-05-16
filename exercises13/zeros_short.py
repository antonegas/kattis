def z(n):
 c=n>-1
 for k in range(1,11):h=10**k;j=h//10;d=(n%h)//j;t=n//h;c+=(j*t-(j-n-1+h*t)*(k>1 and d==0))*(n//j>0)
 return c
while (n:=[*map(int,input().split())])[0]>-1:m,n=n;print(z(n)-z(m-1))
