def seven_seg(x,r=""):
	l=len(x)*3
	for g in range(3*l):r+=" |_|"[(g%3+1)*(((((0xDDFD91EDCD9CD97990F5>>int(x[g%l/3])*8)&255)*2)>>(g%3+g/l*3))&1)]+"\n"[(g+1)%l:]	
	return r