seven_seg=lambda x:''.join([''.join(['_|?'[(int(e,36)>>(int(d)*6)&63)>>2*i&3] for d in str(x) for i in 2,1,0])+'\n' for e in 'K0RPUZ77G1W','5A5R5GSYM7C2','WHOWN6AGEQU'])
