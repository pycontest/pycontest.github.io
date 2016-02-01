def seven_seg(x):
 a=(' _     _  _     _  _  _  _  _ ','| |  | _| _||_||_ |_   ||_||_|','|_|  ||_  _|  | _||_|  ||_| _|')
 r=""
 for i in (0,1,2):
  for t in x:
   g=int(t)*3
   r+=a[i][g:g+3]
  r+="\n"
 return r
