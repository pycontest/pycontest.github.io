n='   .'
m=' _ .'
e='| |.'
a='|_|.'
r='  |.'
l='|  .'
d=' _|.'
s='|_ .'
n=m+e+a,n+r+r,m+d+s,m+d+d,n+a+r,m+s+d,m+s+a,m+r+r,m+a+a,m+a+d
def seven_seg(x):
	a=['']*3
	for d in x:
		l=n[int(d)].split('.')
		for z in range(3):a[z]+=l[z]
	return '\n'.join(a)+'\n'
