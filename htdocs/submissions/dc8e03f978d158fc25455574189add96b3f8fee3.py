d={0:'   ',1:' _ ',2:'  |',3:' _|',4:'|_ ',5:'|_|',6:'| |'};k=0x5f70755464e3039;r=reduce
def f(x,y):
	m=63&(k>>6*int(y));x[0]+=d[1&m];x[1]+=d[((14&m)>>1)+2];x[2]+=d[((48&m)>>4)+2];return x
def seven_seg(x):
	return r(lambda x,y:x+y+'\n',r(f,x,['','','']),'')
