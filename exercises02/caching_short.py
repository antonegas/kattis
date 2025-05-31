from heapq import *
c,n,a=map(int,input().split())
b=[int(input()) for _ in range(a)]
e=[[-a] for _ in range(n)]
for t in range(a-1,-1,-1):e[b[t]]+=[-t]
h=[1]*n
q=[]
m=0
for t in range(a):
 d=b[t];e[d].pop();m+=h[d]
 if h[d] and m>c:_,r=heappop(q);h[r]=1
 h[d]=0;heappush(q,(e[d][-1],d))
print(m)