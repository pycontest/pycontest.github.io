j=''.join
g=lambda p,n,r='|':1<<p&n and r or' '
seven_seg=lambda x:j([j([g(p,a)+g(p,b,'_')+g(p,c) for p in map(int,x)])+'\n' for a,b,c in ((0,1005,0),(881,892,927),(325,877,1019))])