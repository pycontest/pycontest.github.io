t="    _ | |  | _||_||_ 303303333369<<?BB9???9B<9<?9?<"
def seven_seg(x):
	r=""
	for o in 27,17,7:
		for p in x:
			q=ord(t[ord(p)-o])-48;r+=t[q:q+3]
		r+="\n"
	return r
