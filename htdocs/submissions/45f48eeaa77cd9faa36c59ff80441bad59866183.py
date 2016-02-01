def seven_seg(x):
	s=""
	for b in[["0123456789","14","0123456789"],["1237","017","56"],["134579","147","2"]]:
		for c in x:
			for d in[0,1,2]:
				s+="|_|"[d]
				if c in b[d]:s=s[:-1]+" "
		s+="\n"
	return s
