d = [("          ","_ __ _____","          "),("|   ||| ||","  _____ __","|||||  |||"),("| |   | | ","_ __ __ __","|| |||||||")]
def seven_seg(s):
    return '\n'.join([''.join([''.join((x[n],y[n],z[n])) for n in map(int,s)]) for x,y,z in d])+'\n'
