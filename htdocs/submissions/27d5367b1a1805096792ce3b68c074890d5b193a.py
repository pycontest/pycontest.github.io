def seven_seg(s):
 r=''
 for l in[6,3,0]:
  for c in s:
   for v in[4,2,1]:r+=' |_ |'[ord('¯	›9³·‰¿»'[int(c)])>>l&v]
  r+='\n'
 return r
