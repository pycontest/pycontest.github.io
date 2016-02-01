m=' _     _  _     _  _  _  _  _ | |  | _| _||_||_ |_   ||_||_||_|  ||_  _|  | _||_|  ||_| _|'
def seven_seg(x):return '\n'.join([''.join([m[int(i)*3+q:][:3]for i in x])for q in 0,30,60])+'\n'