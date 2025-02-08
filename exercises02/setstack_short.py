l=open(0).readlines();j=1
while j<len(l):
 n=j+1+int(l[j]);s=[];f=s.pop
 for b in l[j+1:n]:s+=[{"P":frozenset,"D":lambda:s[-1],"U":lambda:f()|f(),"I":lambda:f()&f(),"A":lambda:f(-2)|{hash(f())}}[b[:-1][0]]()];print(len(s[-1]))
 print("***");j=n