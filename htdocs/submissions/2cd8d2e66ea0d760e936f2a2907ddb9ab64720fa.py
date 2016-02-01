def seven_seg(x):
	import test_vectors
	s = test_vectors.test_vectors
	return '\n'.join([''.join([s[c].split('\n')[i] for c in x]) for i in range(0, 3)])+'\n'
