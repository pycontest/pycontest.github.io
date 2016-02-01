from test_vectors import*
def seven_seg(x):
	o=''
	for i in range(len(x)):o=''.join([o[j*(1+3*i):j*(1+3*i)+3*i]+test_vectors[x[i]][4*j:4*j+4] for j in 0,1,2])
	return o