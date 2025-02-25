i=input
for _ in range(int(i())):
 l=int(i());n,m=map(int,i().split());r=[i() for _ in range(n+2)];v=set();q=[(r[-1].find("F"),n+1,0)];v.add(q[0])
 while q:
  x,y,t=q.pop(0)
  if r[y][x]=="G":print(f"The minimum number of turns is {t}.");break
  t+=1
  for x,y in [(x,y),(x+1,y),(x,y-1),(x-1,y),(x,y+1)]:
   if not(x<0 or x>=m or y<0 or y>=n+2 or t>l or r[y][(x-((len(r)-1-y)%2*2-1)*t)%len(r[0])]=="X" or (x,y,t%m) in v):v.add((x,y,t%m));q.append((x,y,t))
 else:print("The problem has no solution.")