seven_seg=lambda i:'\n'.join(''.join('| _ | '[p*2:][(r>>3*int(c)+p)&1]for c in i for p in[0,1,2])for r in[766966653,7471706,140555032])+'\n'
