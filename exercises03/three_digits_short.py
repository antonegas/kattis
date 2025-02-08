for i in range(r:=1,int(input())+1):
 r*=i
 while r%10==0:r//=10
 r%=10**12
print(str(r)[-3:])