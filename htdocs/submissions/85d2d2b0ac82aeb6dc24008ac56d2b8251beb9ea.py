def seven_seg(x,s=""):
 for i in [0,1,2]:
  for c in x:
   s+="    _ | ||_|  | _||_ "[int("123044156155034165163144133135"[3*int(c)+i])*3:][:3]
  s+="\n"
 return s
