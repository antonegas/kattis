def get_hiding_places(c,r):
    abc="abcdefgh"
    x = abc.index(c)
    y = int(r)-1

    r8=[*range(8)]

    b = [[-1]*8 for _ in r8]
    b[y][x] = 0

    q=[(x,y,0)]

    while q:
        x, y, t = q.pop(0)
        for x,y in [(x-1, y-2), (x+1, y-2), (x-1, y+2), (x+1, y+2), (x-2, y-1), (x-2, y+1), (x+2, y-1), (x+2, y+1)]:
            if 8>x>=0 and 8>y>=0 and b[y][x]<0:b[y][x]=t+1;q+=[(x,y,t+1)]

    result = list()
    most_moves = 0

    for y in r8[::-1]:
        for x in r8:
            cn = f"{abc[x]}{y+1}"
            m = b[y][x]
            if m>most_moves:
                most_moves=m
                result=[]
            if m==most_moves:
                result+=[cn]

    return f"{most_moves} {' '.join(result)}"

for _ in range(int(input())):print(get_hiding_places(*input()))