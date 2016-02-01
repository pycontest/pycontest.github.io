def seven_seg(x):
    return '\n'.join([''.join(" _     _  _     _  _  _  _  _ "[3*int(c):][:3]
    for c in x),''.join("| |  | _| _||_||_ |_   ||_||_|"[3*int(c):][:3] for
        c in x),''.join("|_|  ||_  _|  | _||_|  ||_| _|"[3*int(c):][:3] for
        c in x), ''])
