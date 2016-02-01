f=[' _|','   ','|_ ','| |',' _ ','|_|','  |']
k="435166402400156420425466455450"
def seven_seg(x): return "\n".join(["".join([f[int(k[3*int(j):3*int(j)+3][i])] for j in x]) for i in [0,1,2]])+"\n"
