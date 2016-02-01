seven_seg=lambda x:'%s\n'*3%tuple(''.join(' _|_| |_   _  |'[(m>>int(d)*3&7)*2:][:3]for d in x)for m in(766954341,164466738,29647089))
