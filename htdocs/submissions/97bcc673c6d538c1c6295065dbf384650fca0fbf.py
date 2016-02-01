def seven_seg(x): return '\n'.join([''.join(s) for s in zip(*[[(' _ ~   ~| |~  |~ _|~|_|~|_ ').split('~')[int(e)] for e in '025133046044153064065033055054'][int(c)*3:int(c)*3+3] for c in x])])+'\n'
