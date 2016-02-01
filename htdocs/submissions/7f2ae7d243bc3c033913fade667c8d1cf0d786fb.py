def seven_seg(x):
 a=b=c="";d="\n"
 for r in x:n=9*ord(r)-432;t=" _ | ||_|     |  | _  _||_  _  _| _|   |_|  | _ |_  _| _ |_ |_| _   |  | _ |_||_| _ |_| _|"[n:n+9];a+=t[:3];b+=t[3:6];c+=t[6:9]
 return a+d+b+d+c+d
