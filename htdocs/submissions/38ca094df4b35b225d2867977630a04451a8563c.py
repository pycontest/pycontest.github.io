def seven_seg(x):
	o=''
	n=[0,1,2]
	for i in n:
		for a in x[:]:
			for j in n: o+=" |_"[(a not in str([x,14,x,1237,170,56,134579,147,2][i*3+j]))*(j%2+1)]
		o+='\n'
	return o
