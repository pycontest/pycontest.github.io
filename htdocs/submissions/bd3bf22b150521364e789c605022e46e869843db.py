def seven_seg(x):
 v={'0':' _ \n| |\n|_|','1':'   \n  |\n  |','2':' _ \n _|\n|_ ','3':' _ \n _|\n _|','4':'   \n|_|\n  |','5':' _ \n|_ \n _|','6':' _ \n|_ \n|_|','7':' _ \n  |\n  |','8':' _ \n|_|\n|_|','9':' _ \n|_|\n _|'};b=''
 for i in range(4):
  for c in x:
   b+=(v[c]+'\n').split('\n')[i]
  if i!=3:
   b+='\n'
 return b
