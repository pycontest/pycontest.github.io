m="     | _  _|| ||_ |_|202202222241336551666153136163"
seven_seg=lambda s:"\n".join(["".join([m[t*3:t*3+3]for t in[int(m[i+int(l)]) for l in s]])for i in(21,31,41)])+"\n"
