d='_| ||_|   |  |_ _||_ _ _| _| |_|  |_|_  _|_|_ |_|_  |  |_|_||_|_|_| _|';seven_seg=lambda n:'\n'.join([''.join(t)for t in zip(*[(' '+d[7*c]+' ',d[7*c+1:7*c+4],d[7*c+4:7*c+7])for c in [ord(x)-48for x in n]])])+'\n'