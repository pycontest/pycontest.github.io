q='| |  | _| _||_||_ |_   ||_||_|'
r='|_|  ||_  _|  | _||_|  ||_| _|'
def seven_seg(x):
	h=j=k=''
	for e in x:
		a=int(e)*3
		b=a+3
		h+=e in('1','4')and'   'or' _ '
		j+=q[a:b]
		k+=r[a:b]
	return h+'\n'+j+'\n'+k+'\n'