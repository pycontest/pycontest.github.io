def seven_seg(o):d,e,f,g,h,j,y=" _ ","|_|"," _|","  |","|_ ","   ","| |";l=[locals()[x] for x in "dyejggdfhdffjegdhfdhedggdeedef"];return "\n".join(["".join([l[int(i)*3+x] for i in o]) for x in 0,1,2])+"\n"