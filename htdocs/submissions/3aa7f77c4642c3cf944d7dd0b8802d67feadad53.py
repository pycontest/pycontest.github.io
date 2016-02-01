def seven_seg(x):
 o=""
 for i in[0,3,6]:
  for d in x:o+=" _ | ||_|     |  | _  _||_  _  _| _|   |_|  | _ |_  _| _ |_ |_| _   |  | _ |_||_| _ |_| _|"[int(d)*9:][i:i+3]
  o+="\n"
 return o
