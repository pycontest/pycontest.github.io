def l(x,y):
 s='';
 for d in x:s+=y[int(d)];
 return s
def seven_seg(x):a=[' _ ','   ',' _ ',' _ ','   ',' _ ',' _ ',' _ ',' _ ',' _ '];b=['| |','  |',' _|',' _|','|_|','|_ ','|_ ','  |','|_|','|_|'];c=['|_|','  |','|_ ',' _|','  |',' _|','|_|','  |','|_|',' _|'];n='\n';return l(x,a)+n+l(x,b)+n+l(x,c)+n
