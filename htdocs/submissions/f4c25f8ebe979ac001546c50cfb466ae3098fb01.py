def seven_seg(x):
 s=[" _ ","   ","| |","  |"," _|","|_|","|_ "]
 t='010010000023445663555364345354'
 r=""
 for i in [0,1,2]:
  r+="".join([s[int(t[int(j)+i*10])] for j in x])+'\n'
 return r
