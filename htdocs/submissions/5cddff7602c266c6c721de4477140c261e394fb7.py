i=int('5acw0gc2xoagkgu3tx4dz61xhyvz',36);t=""
while i:t="_ |"[i%3]+t;i/=3
def seven_seg(x):
 s=""
 for c in x:c=9*int(c);s+=t[c:c+9]
 return((s+'\n\n')*3+'\n')[::3]