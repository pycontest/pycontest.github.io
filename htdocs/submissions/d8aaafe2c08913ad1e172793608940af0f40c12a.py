def seven_seg(x):
 r=''
 x=[[111,9,94,91,57,115,119,73,127,123][int(c)] for c in x]
 for s in ((128,64,128),(32,16,8),(4,2,1)):
  for i in range(len(x)):
   for n in (0,1,2):
    if x[i]-s[n]>=0:
     r+=("|","_","|")[n]
     x[i]-=s[n]
    else:
     r+=" "
  r+="\n"
 return r