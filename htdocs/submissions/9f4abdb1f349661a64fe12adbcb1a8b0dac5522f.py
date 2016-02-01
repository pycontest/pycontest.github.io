seven_seg=lambda x:'%s\n'*3%tuple(''.join(' _|_| |_   _  |'[(m>>int(d)*3&7)*2:][:3]for d in x)for m in(0x2db6cb65,0x9cd9032,0x1c460f1))
