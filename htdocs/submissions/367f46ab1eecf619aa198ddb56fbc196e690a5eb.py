seven_seg=lambda x: '\n'.join([''.join([' _ | ||_|     |  | _  _||_  _  _| _|   |_|  | _ |_  _| _ |_ |_| _   |  | _ |_||_| _ |_| _|'[int(d)*9+p:int(d)*9+p+3]for d in x])for p in(0,3,6)]+[''])
