def seven_seg(x,r='',a=[6,11,2,8,9,9,6,0,4,6,0,0,8,2,9,6,4,0,6,4,2,6,9,9,6,2,2,6,2,0],t=' _|_|_ _   | |'):
	for c in range(3):
		for d in x:
			y=a[int(d)*3+c]
			r+=t[y:y+3]
		r+="\n";
	return r