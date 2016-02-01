def seven_seg(i):
	t,j,k,l,e,p,q,r=['   ',' _ ','| |','  |',' _|','|_ ','|_|'],1005,913762586,645544286,'\n','','',''
	for c in i[:]:
		b=int(c)
		p+=t[j>>b&1]
		q+=t[k>>b*3&7]
		r+=t[l>>b*3&7]
	return p+e+q+e+r+e
