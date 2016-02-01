m=lambda h,e,n,l='|':h>>(e-48)*3&n and l or ' '
seven_seg=lambda s:"".join("".join(m(0x16192106,c,i)+m(0x3f3fafc5,c,i,'_')+m(0x36d26cb6,c,i)for c in map(ord,s))+"\n"for i in(1,2,4))
