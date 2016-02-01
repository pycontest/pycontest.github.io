def seven_seg(x,r=""):
 for k in 0,3,6:
  for n in x:
   j=ord("¯	ž›9³·‰¿»"[int(n)])<<k
   for i in "|_|":
	b=" "
	if j&256:b=i
	r+=b;j*=2
  r+="\n"
 return r