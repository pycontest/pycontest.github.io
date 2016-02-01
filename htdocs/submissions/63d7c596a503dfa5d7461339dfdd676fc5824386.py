m="     | _  _|| ||_ |_|202202222241336551666153136163"
seven_seg=lambda s:"\n".join(["".join([m[t*3:t*3+3]for t in[ord(m[i+ord(l)-27])-48 for l in s]])for i in(0,10,20)])+"\n"
