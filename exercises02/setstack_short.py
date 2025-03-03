s=[];p=print;d="PDUIA"
for l in open(0).readlines()[2:]:l=l[0];f=s.pop;[s:=s+[[frozenset,lambda:s[-1],lambda:f()|f(),lambda:f()&f(),lambda:f(-2)|{hash(f())}][d.index(l)]()],p(len(s[-1]))]if l in d else[p("***"),s:=[]]
p("***")