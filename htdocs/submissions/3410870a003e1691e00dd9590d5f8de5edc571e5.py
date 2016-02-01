def seven_seg(s):return ''.join([''.join([x[3*n:3*n+3] for n in map(int,s)])+'\n' for x in " _     _  _     _  _  _  _  _ ","| |  | _| _||_||_ |_   ||_||_|","|_|  ||_  _|  | _||_|  ||_| _|"])
