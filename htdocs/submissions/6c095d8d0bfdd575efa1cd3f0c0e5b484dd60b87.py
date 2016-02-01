p=' _ | ||_|     |  | _  _||_  _  _| _|   |_|  | _ |_  _| _ |_ |_| _   |  | _ |_||_| _ |_| _|'
j=''.join
seven_seg=lambda s:j([(lambda i:j([p[int(c)*9+x:int(c)*9+x+3]for c in s])+'\n')(x)for x in(0,3,6)])