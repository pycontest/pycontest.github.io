t=' _     _  _     _  _  _  _  _ | |  | _| _||_||_ |_   ||_||_||_|  ||_  _|  | _||_|  ||_| _|'
seven_seg=lambda x:'\n'.join(map(''.join,[[t[j+i*3:j+i*3+3]for i in map(int,x)]for j in 0,30,60]))+'\n'
