segs = [
(" _ ","| |","|_|"),
("   ","  |","  |"),
(" _ "," _|","|_ "),
(" _ "," _|"," _|"),
("   ","|_|","  |"),
(" _ ","|_ "," _|"),
(" _ ","|_ ","|_|"),
(" _ ","  |","  |"),
(" _ ","|_|","|_|"),
(" _ ","|_|"," _|"),
]


def seven_seg(x):
  return ''.join([''.join([segs[int(c)][i] for c in x])+'\n' for i in range(3)])

