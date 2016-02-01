i=int('5acw0gc2xoagkgu3tx4dz61xhyvz',36);t=""
while i:t="_ |"[i%3]+t;i/=3
def seven_seg(x):s="".join([t[9*c:9*c+9]for c in map(int,x)])+'\n'*3;return s[0::3]+s[1::3]+s[2::3]
