z='  |  |||_   ____  |||| '
v='010010000023445663555364345354'
def seven_seg(x):return '\n'.join([''.join(z[int(v[s*10+int(y)])::8] for y in x) for s in 0,1,2])+'\n'
