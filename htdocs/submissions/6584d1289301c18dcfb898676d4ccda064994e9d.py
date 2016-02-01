def seven_seg(x):
 d,m=0x3FBDB545E7F7CDC7ED,lambda y:''.join([' ','_|'[t%2]][d>>(10*t+int(i)+y)&1]for i in x for t in[1,2,3])
 return '\n'.join((''.join(d>>int(i)&1and' _ 'or'   'for i in x),m(0),m(30),''))