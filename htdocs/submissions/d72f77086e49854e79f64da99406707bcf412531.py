def seven_seg(x):
 i=' _ '
 j='|_|'
 k=' _|'
 l='  |'
 m='|_ '
 n='   '
 h=''
 e=[[i,'| |',j],[n,l,l],[i,k,m],[i,k,k],[n,j,l],[i,m,k],[i,m,j],[i,l,l],[i,j,j],[i,j,k]]
 for y in [0,1,2]:
  for z in str(x):
   v=int(z)
   h+=e[v][y]
  h+='\n'
 return h