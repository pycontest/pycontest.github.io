def seven_seg(s):
	g=' _|   | |_|_ _ ';o=3*[''];d='<3<<3<<<<<64008::48884:0408480'
	for c in s:
		for j in 0,1,2:
			i=ord(d[int(c)+j*10])-48;
			o[j]+=g[i:i+3]
	return '\n'.join(o)+'\n'