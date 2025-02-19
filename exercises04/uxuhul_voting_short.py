a=[]
for l in open(0).readlines()[2:]+["0"]:
 if len(p:=[*map(int,l.split())])!=1:a+=[p];continue
 r=[]
 for p in a[::-1]:r=[min([r[b^x] if r else b^x for x in [1,2,4]], key=lambda i:p[i]) for b in range(8)]
 print(["NNN","NNY","NYN","NYY","YNN","YNY","YYN","YYY"][r[0]]);a=[]