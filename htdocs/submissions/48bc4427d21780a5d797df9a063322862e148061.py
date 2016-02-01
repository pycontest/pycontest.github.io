g={0:' '}.get
w=lambda x:g(x&1,'|')+g(x&2,'_')+g(x&4,'|')
def seven_seg(x):
 a=b=c=""
 for z in x:m=0x6fff27be79db5ec8f6>>7*int(z);a+=w(m&2);b+=w(m>>2);c+=w(m>>5)
 return "%s\n"*3%(a,b,c)