seven_seg=lambda x,f=''.join:f(f('    |||  __ __ | || |'[(i/7**int(j)%7)::7]for j in x)+'\n'for i in(94153600,278221864,157233173))