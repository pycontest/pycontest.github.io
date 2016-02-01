def seven_seg(x):
 s=[' _|','   ','|_ ','| |',' _ ','|_|','  |']
 m=[435,166,402,400,156,420,425,466,455,450]
 k=''
 for l in [0,1,2]: 
  for n in x:
   k+=s[int(str(m[int(n)])[l])]
  k+='\n'
 return k
