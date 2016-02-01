def seven_seg(x):
	v = " _ | ||_|     |  | _  _||_  _  _| _|   |_|  | _ |_  _| _ |_ |_| _   |  | _ |_||_| _ |_| _|"
	return ''.join([ ''.join([v[((int(a)+1)*9)-9:((int(a)+1)*9)-6] for a in x] +['\n']+ [v[((int(a)+1)*9)-6:((int(a)+1)*9)-3] for a in x] +['\n']+ [v[((int(a)+1)*9)-3:(int(a)+1)*9] for a in x] + ['\n']) ])
