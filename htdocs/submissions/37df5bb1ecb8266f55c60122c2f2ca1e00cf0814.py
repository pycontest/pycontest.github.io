def seven_seg(x):
 s=''
 for i in 0,10,20:
  for c in x:
   for k in 0,1,2:s+=int("202202222254667334777436467476"[i+int(c)])&(1<<k) and '|_|'[k] or ' '
  s+='\n'
 return s