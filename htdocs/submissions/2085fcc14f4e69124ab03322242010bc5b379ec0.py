def seven_seg(s):
  A,B,C,D,E,F,a,b,c=' _ ','   ','  |',' _|','|_ ','|_|',[],[],[];n=((A,'| |',F),(B,C,C),(A,D,E),(A,D,D),(B,F,C),(A,E,D),(A,E,F),(A,C,C),(A,F,F),(A,F,D))
  def j(v):return ''.join(v)+'\n'
  def h(k,l,m):k.append(n[l][m])
  for i in list(s):i=int(i);h(a,i,0);h(b,i,1);h(c,i,2)
  return j(a)+j(b)+j(c)
