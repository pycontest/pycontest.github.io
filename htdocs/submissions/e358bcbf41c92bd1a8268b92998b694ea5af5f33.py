def seven_seg(x,o='',z='|_ _ _| |_|   |',p=0x482882CC2802402C8B442042CCB862):
	for y in[0,1,2]:
		for n in x:t=(((p>>(int(n)*12))%4096)>>(4*y))%16;o+=z[t:t+3]
		o+='\n'
	return o
