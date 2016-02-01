z = [' _ ','   ','| |','  |',' _|','|_|','|_ '];v=['0100100000','2344566355','5364345354']
def seven_seg(x):
 return '\n'.join([''.join([z[int(v[s][int(y)])] for y in x]) for s in range(3)])+'\n'

