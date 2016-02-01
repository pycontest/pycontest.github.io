def seven_seg(x):
 s='';t='   _  | |_ _|_|136022154155062145146122166165'
 for i in 0,1,2:
  for c in x:j=int(t[15+int(c)*3+i])*2;s+=t[j:j+3]
  s+='\n'
 return s
