def seven_seg(x):
 a=(' _     _  _     _  _  _  _  _ ','| |  | _| _||_||_ |_   ||_||_|','|_|  ||_  _|  | _||_|  ||_| _|')
 s=""
 for i in (0,1,2):
  for t in x:
   g=int(t)*3
   s+=a[i][g:g+3]
  s+="\n"
 return s 


