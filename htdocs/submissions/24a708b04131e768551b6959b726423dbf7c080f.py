def seven_seg(x):
 v={'0':'_ .| |.|_|','1':'  .  |.  |','2':'_ . _|.|_ ','3':'_ . _|. _|','4':'  .|_|.  |','5':'_ .|_ . _|','6':'_ .|_ .|_|','7':'_ .  |.  |','8':'_ .|_|.|_|','9':'_ .|_|. _|'};b=''
 for i in range(4):
  for c in x:
   s=' '+v[c]+'.'
   b+=s.split('.')[i]
  if i!=3:
   b+='\n'
 return b