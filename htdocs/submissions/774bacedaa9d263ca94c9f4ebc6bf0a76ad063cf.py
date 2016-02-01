a='|_|'
b='  |'
c='|_ '
d=' _|'
e=' _ '
f='   '
g='| |'
v=('efe'*2+'e'*4,'gbddaccbaa','abcdbdabad') 
def seven_seg(x):return '\n'.join([''.join([eval(v[i][int(z)])for z in x])for i in(0,1,2)])+'\n'