a,b,c,d,e,f,g=' _|','  |','   ',' _ ','|_ ','|_|','| |'
def seven_seg(s):
	X=[]
	for l in (0,1,2):
		for z in s:X+=''.join(((d,g,f),(c,b,b),(d,a,e),(d,a,a),(c,f,b),(d,e,a),(d,e,f),(d,b,b),(d,f,f),(d,f,a))[int(z)][l])
		X+='\n'
	return ''.join(X)