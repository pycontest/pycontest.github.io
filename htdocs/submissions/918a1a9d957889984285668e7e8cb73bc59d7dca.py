z='  |  |||_   ____  |||| '
v='010010000023445663555364345354'
j=''.join
def seven_seg(x):return j([j(z[int(v[r*10+int(d)])::8] for d in x)+'\n' for r in 0,1,2])
