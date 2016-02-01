a,b,c,d,e,f,g=' _|','  |','   ',' _ ','|_ ','|_|','| |'
D={'0':(d,g,f),'1':(c,b,b),'2':(d,a,e),'3':(d,a,a),'4':(c,f,b),'5':(d,e,a),'6':(d,e,f),'7':(d,b,b),'8':(d,f,f),'9':(d,f,a)}
def seven_seg(s):
	X = []
	for l in (0,1,2):
		for c in s:X += ''.join(D[c][l])
		X+='\n'
	return ''.join(X)