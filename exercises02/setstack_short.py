def p(s):
 s+=[frozenset()]
def d(s):
 s+=[s[-1]]
def u(s):
 a=s.pop();b=s.pop();s+=[a|b]
def i(s):
 a=s.pop();b=s.pop();s+=[a&b]
def a(s):
 a=s.pop();b=s.pop();s+=[b|{hash(a)}]
o="";l=open(0,"r").readlines();j=1
while j<len(l):
 n=j+1+int(l[j]);j+=1;x=[]
 for b in l[j:n]:
  t={"P":p,"D":d,"U":u,"I":i,"A":a};t[b[:-1][0]](x);o+=f"{len(x[-1])}\n"
 o+="***\n";j=n
open(1,"w").write(o)