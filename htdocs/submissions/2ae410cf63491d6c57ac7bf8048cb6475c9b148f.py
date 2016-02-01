from test_vectors import test_vectors
def seven_seg(x):
  return '\n'.join([''.join([a[i] for a in [b.split('\n') for b in [c for c in [test_vectors[x[y]] for y in range(0,len(x))]]]]) for i in range(0,4)])
