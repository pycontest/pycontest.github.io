def seven_seg(a):
	b=tuple;c=b(" |_X|")
	def d(e):return c[e&4]+c[e&2]+c[e&1]
	def f(g):
		h=""
		for i in b(a):h+=d(int(b("%o"%g)[int(i)]))
		return h+"\n"
	return f(273163410)+f(695200895)+f(969719419)
