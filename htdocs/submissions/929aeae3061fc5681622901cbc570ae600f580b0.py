r=192205843403787414087;g=' _ ?   ?| |?  |? _|?|_|?|_ '.split("?");u=7**10
f=lambda s,n: "".join([g[((r/u**n%u)/(7**(ord(o)-48)))%7] for o in s])+"\n"
def seven_seg(x):return f(x,2)+f(x,1)+f(x,0)
