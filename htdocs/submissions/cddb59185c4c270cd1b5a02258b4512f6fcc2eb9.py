def seven_seg(x):return ''.join([''.join(x)+'\n'for x in zip(*[["    _   | _||  |_ | ||_|"[int(i)*3:][:3]for i in l]for l in[list("167022135133072153157122177173"[int(n)*3:][:3])for n in x]])])
