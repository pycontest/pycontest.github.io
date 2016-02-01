def seven_seg(a):
 b=tuple;c=b(" |_X|")
 def f(g):
	h=""
	for i in b(a):h+=(lambda e:c[e&4]+c[e&2]+c[e&1])(int(b("%o"%g)[int(i)]))
	return h+"\n"
 return f(273163410)+f(695200895)+f(969719419)
