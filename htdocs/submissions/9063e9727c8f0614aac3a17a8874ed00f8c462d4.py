def seven_seg(x):f=lambda d:''.join(' |  | |__ __   |||  |'[d>>3*int(c)&7::7]for c in x)+'\n';return f(20520)+f(156374742)+f(423995153)