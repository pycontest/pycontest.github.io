def seven_seg(x):
	s,r=" |_ |",""
	for p in 0,1,2:
		for c in x:j=int("257011236233071263267211277273"[int(c)*3+p]);r+=s[j&4]+s[j&2]+s[j&1]
		r+="\n"
	return r
