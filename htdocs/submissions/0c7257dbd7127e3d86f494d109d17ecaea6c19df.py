def seven_seg(i):
 s=''
 for r in 0,3,6:
  for l in i:
   for x in r,r+1,r+2:
    s+=' _ |_||_|'[0x1BBFB23DB9B39B2F321EA>>8*int(l)+x&1 and x]
  s+='\n'
 return s
