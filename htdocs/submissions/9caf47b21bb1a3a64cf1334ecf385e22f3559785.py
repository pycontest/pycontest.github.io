def seven_seg(s): 
 t='  |','|_ ',' _|','|_|','| |';l=m=n='';f='\n'
 for c in s:i=ord(c)-48;l+='   _  '[1005>>i&1::2];m+=t[453293188>>i*3&7];n+=t[735379>>i*2&3]
 return l+f+m+f+n+f