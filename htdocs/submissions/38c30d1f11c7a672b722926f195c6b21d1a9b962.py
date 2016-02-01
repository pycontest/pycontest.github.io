def seven_seg(x):
 a,r,l=" _      | _||_||_ | |","","010010000062334552444253234243"
 for u in [0,1,2]:
  for i in x:
   b=int(eval(l[u*10+int(i)]))
   r+=a[b*3:b*3+3]
  r+="\n"
 return r
