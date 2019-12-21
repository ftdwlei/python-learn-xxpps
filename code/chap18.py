# random使用
# author:capatain
import random

menus=('姜母鸭','十全药炖排骨肉','骨茶新加坡肉','骨茶党参鸡汤','宫廷镬仔浸鸡子','希腊风味牛肉汤','韩式的人参鸡汤')
listmenus=list(menus)
print("全部有"+str(len(listmenus))+"款菜品"+str(listmenus))
num=int(input("请抽取免费菜品（0-"+str(len(listmenus)-1)+"):"))
random.shuffle(listmenus)
print("第一款免费菜品是"+listmenus[num])
num=int(input("请抽取免费菜品（0-"+str(len(listmenus)-1)+"):"))
random.shuffle(listmenus)
print("第二款免费菜品是"+listmenus[num])