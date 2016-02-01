def seven_seg(x,o=''):
	for z in[0,3,6]:
		for c in x:
			for y in[1,2,3]:o+=' |_|'[(0x375fa9176b3538d93ca41ea>>(9*int(c)+z+y-1)&1)*y]
		o+='\n'
	return o
