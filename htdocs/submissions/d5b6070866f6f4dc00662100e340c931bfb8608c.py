seven_seg=lambda x:"\n".join("".join(' |'[b/4&1]+'  _'[b&2]+' |'[b&1]for b in[i>>3*int(e)for e in x])for i in[306775170,1060861645,524130191])+'\n'