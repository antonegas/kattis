f=lambda:s.pop()
def p(s):s+=[frozenset()]
def d(s):s+=[s[-1]]
def u(s):a=f();b=f();s+=[a|b]
def i(s):a=f();b=f();s+=[a&b]
def a(s):a=f();b=f();s+=[b|{hash(a)}]
o="";l=open(0).readlines();j=1;t={"P":p,"D":d,"U":u,"I":i,"A":a}
while j<len(l):
 n=j+1+int(l[j]);j+=1;s=[]
 for b in l[j:n]:t[b[:-1][0]](s);o+=f"{len(s[-1])}\n"
 o+="***\n";j=n
open(1,"w").write(o)