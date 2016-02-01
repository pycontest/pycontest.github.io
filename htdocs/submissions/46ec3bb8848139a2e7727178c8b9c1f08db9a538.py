def seven_seg(n,y=''):
 for l in '0800800000','b922466944','4962924942':
  for c in (eval('0x%s'%l[int(d)]) for d in n):y+=' _ _|_|_   | |'[c:c+3]
  y+='\n'
 return y