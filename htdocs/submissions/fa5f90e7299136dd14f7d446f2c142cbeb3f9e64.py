z='   '
y=' _ '
x='  |'
w='|_|'
v=' _|'
u='|_ '
a=(y,'| |',w),(z,x,x),(y,v,u),(y,v,v),(z,w,x),(y,u,v),(y,u,w),(y,x,x),(y,w,w),(y,w,v)
seven_seg=lambda s:'\n'.join(''.join(a[int(x)][i]for x in s)for i in range(3))+'\n'