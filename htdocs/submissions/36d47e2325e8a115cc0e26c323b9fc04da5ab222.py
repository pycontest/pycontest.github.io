def seven_seg(x):
	s=lambda p,v:1<<p&(125,80,55,87,90,79,111,81,127,95)[v]>0;s0=['   ',' _ '];s3=s4=s5=s6=[' ','|'];s1=s2=[' ','_'];f=''
	for r in [[0],[3,1,4],[5,2,6]]:
		for d in x:
			for p in r:f+=eval('s%s[%s]'%(p,s(p,int(d))))
		f+='\n'
	return f
