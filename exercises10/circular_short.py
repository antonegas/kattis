import math;i=input;j=int(i())
while j:a,b,p,q,c,d,r,s=map(int,(i()+" "+i()).split());print("No"if(a-b-c+d)%math.gcd(p,q,r,s)else"Yes");j-=1