d='_| ||_|   |  |_ _||_ _ _| _| |_|  |_|_  _|_|_ |_|_  |  |_|_||_|_|_| _|';seven_seg=lambda n:'\n'.join([''.join(t)for t in zip(*[(' '+d[c]+' ',d[c+1:c+4],d[c+4:c+7])for c in [7*(ord(x)-48)for x in n]])])+'\n'