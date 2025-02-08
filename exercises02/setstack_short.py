s=[]
for l in open(0).readlines()[2:]:l=l[0];f=s.pop;d={"P":frozenset,"D":lambda:s[-1],"U":lambda:f()|f(),"I":lambda:f()&f(),"A":lambda:f(-2)|{hash(f())}};[s:=s+[d[l]()],print(len(s[-1]))] if l in d else [print("***"),s:=[]]
print("***")