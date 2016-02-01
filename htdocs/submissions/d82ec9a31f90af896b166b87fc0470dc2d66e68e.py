def seven_seg(x):
    a='|_|'
    b='  |'
    c='|_ '
    d=' _|'
    e=' _ '
    f='   '
    g='| |'
    v=('efe'*2+'e'*4,'gbddaccbaa','abcdbdabad') 
    return '\n'.join([''.join([eval(v[i][int(z)])for z in x])for i in(0,1,2)])+'\n'