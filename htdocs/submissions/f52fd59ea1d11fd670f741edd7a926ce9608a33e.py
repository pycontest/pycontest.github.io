def seven_seg(x):
 a,b,c,d,e,f,g,r=" _ ","   ","  |"," _|","|_|","|_ ","| |","";l="abaabaaaaagcddeffceeecfdcdeced"
 for u in [0,1,2]:
  for i in x:
   r+=eval(l[u*10+int(i)])
  r+="\n"
 return r
