from collections import *
def frogger(l,n,m,r):
    v=set();q=deque();x=r[-1].find("F");s=(x,n+1,0);v.add((x,n+1,0));q.append(s)

    while q:
        x,y,t=q.popleft()

        if t>l:continue

        if r[y][x]=="G":return t

        for nx, ny, nt in [(x+dx,y+dy,t+1) for dx, dy in [(0,0),(1,0),(0,-1),(-1,0),(0,1)]]:
            if nx < 0 or nx >= m or ny < 0 or ny >= n + 2:
                continue

            if r[ny][(nx-((len(r)-1-ny)%2*2-1)*nt)%len(r[0])]=="X":
                continue

            if (nx,ny,nt%m) in v:
                continue

            v.add((nx,ny,nt%m))
            q.append((nx, ny, nt))

    return -1

for _ in range(int(input())):x=int(input());n,m=map(int,input().split());r=[input() for _ in range(n+2)];t=frogger(x,n,m,r);print("The problem has no solution.") if t<0 else print(f"The minimum number of turns is {t}.")