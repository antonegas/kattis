def p(s):s+=[frozenset()]
def d(s):s+=[s[-1]]
def u(s):a=f();b=f();s+=[a|b]
def i(s):a=f();b=f();s+=[a&b]
def a(s):a=f();b=f();s+=[b|{hash(a)}]
l=open(0).readlines();j=1;f=lambda:s.pop()
while j<len(l):
 j+=1;n=j+int(l[j-1]);s=[]
 for b in l[j:n]:{"P":p,"D":d,"U":u,"I":i,"A":a}[b[:-1][0]](s);print(len(s[-1]))
 print("***");j=n