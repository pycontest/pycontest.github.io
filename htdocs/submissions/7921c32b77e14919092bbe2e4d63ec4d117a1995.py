def seven_seg(x):
	l="| "
	u="_ "
	q=w=e='\n'
	while x:
		a=x[-1]
		x=x[:-1]
		q=' '+u[a in "14"]+' '+q
		w=l[a in "1237"]+u[a in "017"]+l[a in "56"]+w
		e=l[a in "134579"]+u[a in "147"]+l[a=='2']+e
	return q+w+e
