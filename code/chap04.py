# 输入输出练习
# author：captain

print("=======本店今日提供以下品种=========")
print("#      1.香橙磅蛋糕               #")
print("#      2.腊肠咸蛋糕               #")
print("#      3.黑芝麻糖霜蛋糕           #")
print("#      4.大理石咕咕洛夫奶油蛋糕    #")

num=int(input("请输入序号查询蛋糕价格："))
if num==1:
    print("1.香橙磅蛋糕 ，单价：",15)
elif num==2:
    print("2.腊肠咸蛋糕 ，单价：", 15)
elif num==3:
    print("3.黑芝麻糖霜蛋糕，单价：", 15)
elif num==4:
    print("4.大理石咕咕洛夫奶油蛋糕，单价：", 15)
else:
    print("wrong number!")