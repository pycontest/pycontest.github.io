def seven_seg(x,o=''):
	for z in[6,3,0]:
		for c in x:
			for y in[2,1,0]:o+=[' ','|_|'[y]][0x176bf44add66394da7812af>>(int(c)*9+z+y)&1]
		o+='\n'
	return o
