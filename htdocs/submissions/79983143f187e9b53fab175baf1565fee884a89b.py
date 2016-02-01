c='   | || _ __ _  | |||'
t='101101111152446332666234246264'
seven_seg=lambda x:'\n'.join(map(''.join,[[c[int(t[j+i])::7]for i in map(int,x)]for j in 0,10,20]))+'\n'