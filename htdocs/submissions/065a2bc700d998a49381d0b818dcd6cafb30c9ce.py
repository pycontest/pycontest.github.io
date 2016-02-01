def seven_seg(x):
 r=''
 for i in [0,1,2]:
  for c in x:
   j=int("125033146144053164165133155154"[int(c)*3+i])*3
   r+="    _ | |  | _||_||_ "[j:j+3]
  r+="\n"
 return r
