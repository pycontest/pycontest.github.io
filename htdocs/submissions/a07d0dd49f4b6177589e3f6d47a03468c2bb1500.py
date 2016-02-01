a,b,c,d,e,f,n='   ',' _ ','|_|',' _|','|_ ','  |','\n'
u,m,g=[b,a,b]*2+[b]*4,['| |',f,d,d,c,e,e,f,c,c],[c,f,e,d,f,d,c,f,c,d]
def seven_seg(x):l=lambda j:''.join([j[int(i)] for i in x]);return l(u)+n+l(m)+n+l(g)+n
