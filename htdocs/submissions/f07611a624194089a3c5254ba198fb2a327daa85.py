a='|_|';b=' _|';c='|_ ';d='  |';e=' _ ';f='   '
v=[[e,'| |',a],[f,d,d],[e,b,c],[e,b,b],[f,a,d],[e,c,b],[e,c,a],[e,d,d],[e,a,a],[e,a,b]]
def seven_seg(x):return ''.join([(''.join([v[int(j)][i] for j in x])+"\n") for i in [0,1,2]])
