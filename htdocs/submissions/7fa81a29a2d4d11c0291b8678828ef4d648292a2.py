def seven_seg(x,i=0x3fbdb545e7f7cdc400fb400,o=''):
	while i:
		for t in x:
			n=i
			for j in'|_|':o+=(' '+j)[n>>int(t)&1];n>>=10
		o+='\n';i>>=30
	return o
