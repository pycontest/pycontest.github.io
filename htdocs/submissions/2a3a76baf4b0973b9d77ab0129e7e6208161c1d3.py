seven_seg=lambda x:"\n".join("".join(" _ | ||_|  | _||_    "[int(oct(0x159B12893262C1506C2414)[int(c)*3+i])*3:][:3]for c in x)for i in[0,1,2])+"\n"