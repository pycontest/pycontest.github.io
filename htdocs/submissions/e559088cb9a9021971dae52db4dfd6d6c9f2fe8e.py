def seven_seg(x):
 a=''
 for r in ' _     _  _     _  _  _  _  _ ','| |  | _| _||_||_ |_   ||_||_|','|_|  ||_  _|  | _||_|  ||_| _|':
  for c in x:
   i=ord(c)*3-144
   a+=r[i:i+3]
  a+='\n'
 return a
