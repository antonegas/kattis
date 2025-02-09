for l in open(0).readlines():
 l=int(l);r=""
 while l:r+=str([0,1,2,5,9,8,6][l%7]);l//=7
 print(r)