def seven_seg(i,m=''):
 for s in'5455455555','2600133611','1630601610':
	for k in i:j=int(s[int(k)])*2;m+=' _|_| |_   _  |'[j:j+3]
	m+='\n'
 return m