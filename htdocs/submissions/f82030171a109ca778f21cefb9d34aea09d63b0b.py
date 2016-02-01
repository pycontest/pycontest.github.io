t=' _     _  _     _  _  _  _  _ | |  | _| _||_||_ |_   ||_||_||_|  ||_  _|  | _||_|  ||_| _|'
def seven_seg(x):
 l=['','','']
 for i in map(int,x):
  for j in [0,30,60]:l[j/30]+=t[j+i*3:j+i*3+3]
 return '\n'.join(l)+'\n'
