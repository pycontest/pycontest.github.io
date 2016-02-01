def seven_seg(x):
 s,r=' _    | |  | _||_||_ 010010000023445663555364345354',""
 for i in [0,1,2]:
  r+="".join([s[t:t+3] for t in [3*int(s[i*10+int(j)+21]) for j in x]])+'\n'
 return r
