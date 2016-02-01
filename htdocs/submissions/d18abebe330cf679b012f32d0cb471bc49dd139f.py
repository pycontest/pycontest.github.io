def seven_seg(i):
	u,v,w,e,p,q,r=' _     _  _     _  _  _  _  _ ','| |  | _| _||_||_ |_   ||_||_|','|_|  ||_  _|  | _||_|  ||_| _|','\n','','',''
	for c in i[:]:
		d=int(c)*3
		p+=u[d:d+3]
		q+=v[d:d+3]
		r+=w[d:d+3]
	return p+e+q+e+r+e
