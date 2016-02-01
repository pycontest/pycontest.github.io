def seven_seg(n):
	o=(0,8,0,0,8,0,0,0,0,0),(11,9,2,2,4,6,6,9,4,4),(4,9,6,2,9,2,4,9,4,2);x=''
	for l in o:
		for c in (l[int(d)] for d in n):x+=' _ _|_|_   | |'[c:c+3]
		x+='\n'
	return x