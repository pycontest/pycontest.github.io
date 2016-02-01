def seven_seg(x):
	s=['']*4
	def q(i,n):s[i]+='   _ _|_|_  | |  '[2*n:2*n+3]
	for h in x:k=ord("=ZE%V)9[7'"[int(h)]);q(1,k>>1&7),q(2,k>>4&7),q(0,k&1)
	return'\n'.join(s)
