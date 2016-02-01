def seven_seg(x):
	l=['']*4
	for c in x:
		for i in range(9):l[i/3]+=(' _ |_||_|'[i]+' ')[c in str((0,14,0,1237,170,56,134579,147,2)[i])]
	return '\n'.join(l)
