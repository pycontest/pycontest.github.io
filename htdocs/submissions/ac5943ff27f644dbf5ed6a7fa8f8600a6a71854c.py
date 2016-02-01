def seven_seg(x):
 d={'a':' _ ','b':'|_|','c':' _|','d':'|_ ','e':'| |','f':'   ','g':'  |',0:'aeb',1:'fgg',2:'acd',3:'acc',4:'fbg',5:'adc',6:'adb',7:'agg',8:'abb',9:'abc'}
 def s(i):return ''.join([d[d[int(w)][i]]for w in x])
 return '%s\n%s\n%s\n'%(s(0),s(1),s(2)) 
 
