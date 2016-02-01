def seven_seg(m):
    r=str()
    for l in range(3):
        for i in range(len(m)):
            r+=g(int(m[i]),l)
        r+='\n'
    return r
def g(d, l):
    n=[' _     _  _     _  _  _  _  _ ','| |  | _| _||_||_ |_   ||_||_|','|_|  ||_  _|  | _||_|  ||_| _|']
    return n[l][(d*3):(d*3+3)]
 
