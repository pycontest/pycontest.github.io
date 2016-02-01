d={'0':'   ','1':' _ ','2':'  |','3':' _|','4':'|_ ','5':'|_|','6':'| |'};k='101101111162335442555243235253'
def f(x,y):
	i = int(y);x[0]+=d[k[i]];x[1]+=d[k[i+10]];x[2]+=d[k[i+20]];return x
def seven_seg(x):
	return reduce(lambda x,y:x+y+'\n',reduce(f,x,['','','']),'')
