def g(p,ts,sr):
    s=[p[0]];i=1;t=sr
    while t<ts[-1]:
        while t>ts[i]:i+=1
        px,py=p[i];qx,qy=p[i-1];h=t-ts[i-1];dt=ts[i]-ts[i-1];rx=qx+(px-qx)*(h/dt);ry=qy+(py-qy)*(h/dt);s+=[(rx,ry)];t+=sr
    s+=[p[-1]]
    return s
def f(ps):
    d = 0
    for p, q in zip(ps, ps[1:]):
        px,py=p
        qx,qy=q
        d += ((px-qx)**2+(py-qy)**2)**0.5
    return d
n, t = map(int, input().split())
ps = list()
ts = list()
for _ in range(n):
    x, y, time = map(int, input().split())
    ps.append((x, y))
    ts.append(time)
gp = g(ps, ts, t)
a = f(ps)
gps = f(gp)
d = abs(a - gps)
print((d / a) * 100)