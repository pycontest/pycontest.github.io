def seven_seg(x):return'\n'.join(''.join(r[int(d)*3:int(d)*3+3]for d in x)for r in[' _     _  _     _  _  _  _  _ ','| |  | _| _||_||_ |_   ||_||_|','|_|  ||_  _|  | _||_|  ||_| _|'])+'\n'
