def seven_seg(x):
 l=(' _ ','   ','  |','| |','|_|','|_ ',' _|')
 t=('034','122','065','066','142','056','054','022','044','046')
 r=''
 for i in (0,1,2):
  for j in x:r+=l[int(t[int(j)][i])]
  r+='\n'
 return r
