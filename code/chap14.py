# 循环
# author:capatain

#完成一个九九口诀表
for i in range(1,10):
    for j in range(1,i+1):
        print("%dx%d=%-2d"%(j,i,i*j),end=' ')
    print()