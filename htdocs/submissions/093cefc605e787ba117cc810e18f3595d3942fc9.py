def seven_seg(x):
	a=b=c='\n'
	f='| |  | _| _||_||_ |_   ||_||_|  ||_  _|  | _||_|  ||_| _|'
	for d in x[::-1]:
		i=3*int(d)
		a,b,c=' '+f[34-i]+' '+a,f[i:i+3]+b,f[i+27:i+30]+c
	return a+b+c
