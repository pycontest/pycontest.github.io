seven_seg=lambda x:''.join(''.join(' _ _|_| |_    |'[int(m,36)/7**int(d)%7*2:][:3]for d in x)+'\n'for m in('9ag','1m6i41','xzo4p'))
