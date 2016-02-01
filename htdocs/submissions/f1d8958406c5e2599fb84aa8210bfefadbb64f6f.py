def seven_seg(x,o=''):
	for y in[0,1,2]:
		for n in x:t=(0x482882CC2802402C8B442042CCB862>>int(n)*12%4096>>4*y)%16;o+='|_ _ _| |_|   |'[t:t+3]
		o+='\n'
	return o
