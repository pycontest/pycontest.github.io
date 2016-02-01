a,b,c,d,e,f,g=' _|','  |','   ',' _ ','|_ ','|_|','| |'
D = ((d,g,f),(c,b,b),(d,a,e),(d,a,a),(c,f,b),(d,e,a),(d,e,f),(d,b,b),(d,f,f),(d,f,a))
def seven_seg(s):
	X = []
	for l in (0,1,2):
		for c in s:X += ''.join(D[int(c)][l])
		X+='\n'
	return ''.join(X)