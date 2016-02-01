def seven_seg(x,r=''):
 for i in 0,1,2:
  for l in x:j=int(l)*3;c=int('034122065066142056054022044046'[j:][i])*2;r+=' _    | |_|_ _|'[c:c+3]
  r+='\n'
 return r