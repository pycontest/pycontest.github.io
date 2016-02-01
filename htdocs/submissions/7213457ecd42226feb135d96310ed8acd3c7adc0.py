import re
def seven_seg(x):
 z=[0,14,0,1237,170,56,134579,147,2];e='\n';f=' _ |_||_|';h=i=j=''
 for d in x:
  a=''
  for g in range(9):
   if re.search(d,str(z[g])):
    a+=' '
   else:
    a+=f[g]
  h+=a[:3];i+=a[3:6];j+=a[6:]
 return h+e+i+e+j+e
