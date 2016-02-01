t=1,2,3
seven_seg=lambda s:'\n'.join(''.join(' |_|'[(0x375fa9176b3538d93ca41ea0>>int(c)*9+n*3+x&1)*x]for c in s for x in t)for n in t)+'\n'