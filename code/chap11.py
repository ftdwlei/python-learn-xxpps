# if嵌套
# author :captain

ans=input("作业做完了吗？(Y或N)")
if ans=='Y':
    print("欢迎您，王者。请进入游戏！")
    age=int(input("请问王者，您几岁？（0-150）"))
    if age>0 and age<12:
        print("您只能玩一个小时哦！")
    elif age<18:
        print("您只能玩二个小时哦！")
    elif age<150:
        print("你是成年人了，自己控制时间！")
    else:
        print("别闹！你输入的不是人的年龄！")
elif ans=='N':
    print("想什么呢，赶紧滚回去写作业！")
else:
    print("答非所问！")