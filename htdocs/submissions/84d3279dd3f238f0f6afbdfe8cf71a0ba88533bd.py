def seven_seg(x):
	r=''
	for i in 0,1,2:
		for h in x:k=ord("=ZE%V)9[7'"[int(h)]);n=[k*2&2,k&14,k/8&14][i];r+='   _ _|_|_  | |'[n:n+3]
		r+='\n'
	return r
