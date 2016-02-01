def seven_seg(x):
 a,b,c,d,e,f,r=" _ ","   ","  |"," _|","|_|","|_ ","";l=[[a,b,a,a,b,a,a,a,a,a],["| |",c,d,d,e,f,f,c,e,e],[e,c,f,d,c,d,e,c,e,d]]
 for u in [0,1,2]:
  for i in x:
   r+=l[u][int(i)]
  r+="\n"
 return r
