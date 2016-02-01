S='     | _  _||  | ||_ |_|202202222251337661777163137173'
def seven_seg(x):
	def d(o):j=int(c)+o;j=int(S[j])*3;return S[j:j+3]
	t=m=b=""
	for c in x: t+=d(24);m+=d(34);b+=d(44)
	return t+"\n"+m+"\n"+b+"\n"
