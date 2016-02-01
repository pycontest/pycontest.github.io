def seven_seg(x):
 a,t,s=[175,9,158,155,57,179,183,137,191,187],'|_||_| _ ',""
 def b(y,z): return (y>>z)&((1<<1)-1)
 def c(y,z):
  if b(191,z)&b(a[int(y)],z):return t[z]
  else:return " "
 for i in (0,3,6):
  for q in x:
   for j in [8,7,6]: s = "%s%s" % (s,c(q,j-i))
  s = "%s%s" % (s,"\n")
 return s
