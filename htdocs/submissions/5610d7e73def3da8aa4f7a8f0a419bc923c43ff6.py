def seven_seg(x):
 v=['_ .| |.|_|','  .  |.  |','_ . _|.|_ ','_ . _|. _|','  .|_|.  |','_ .|_ . _|','_ .|_ .|_|','_ .  |.  |','_ .|_|.|_|','_ .|_|. _|'];b=''
 for i in range(4):
  for c in x:
   b+=((' '+v[int(c)]+'.').split('.'))[i]
  if i!=3:
   b+='\n'
 return b