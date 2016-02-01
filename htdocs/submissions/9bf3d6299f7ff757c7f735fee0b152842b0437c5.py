j=''.join
w,i,u,r=' |_\n'
g=lambda p,n,r=i:1<<p&n and r or w
seven_seg=lambda x:j([j([g(p,a)+g(p,b,u)+g(p,c) for p in map(int,x)])+r for a,b,c in ((0,1005,0),(881,892,927),(325,877,1019))])