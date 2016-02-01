def seven_seg(x,r="",q=[0,1,2]):
 for i in q:
  for c in str(x):
   for j in q:
    r+=["|_|"[j]," "][1<<int(c)&[65535,18,65535,142,131,96,698,146,4][i*3+j]>0]
  r+="\n"
 return r
