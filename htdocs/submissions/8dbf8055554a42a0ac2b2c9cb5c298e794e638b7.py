import re
seven_seg=lambda s:'\n'.join(''.join(re.findall('.{3}',' _ | ||_|     |  | _  _||_  _  _| _|   |_|  | _ |_  _| _ |_ |_| _   |  | _ |_||_| _ |_| _|')[int(x)*3+i]for x in s)for i in range(3))+'\n'