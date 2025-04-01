for l in open(0):
 l=int(l);r=""
 while l:r+="0125986"[l%7];l//=7
 print(r)