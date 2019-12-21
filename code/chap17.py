# 函数，搭建房屋
# author :captain


def print_building(w,h,level):
    print_floor(w)
    for i in range(level):
        print_wall(w,h)
        print_floor(w)

def print_floor(w):
    print('-'*w)

def print_wall(w,h):
    for j in range(h):
        print('|'+' '*(w-2)+'|')

w=int(input("请输入房屋的宽度："))
h=int(input("请输入房屋的高度："))
level=int(input("请输入房屋的层数："))
print_building(w,h,level)