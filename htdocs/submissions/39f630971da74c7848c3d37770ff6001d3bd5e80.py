def seven_seg(x,r=""):
 for i in 4104,458374549,860826899:
  for c in str(x):r+=" _      ||_||_ | | _|"[(i>>int(c)*3&7)*3:][:3]
  r+="\n"
 return r