# 优惠金额计算
# author：captain
while 1:
    spends=int(input("请输入购买总价："))
    if spends<=0:
        break
    if spends<=100:
        return_money=spends*0.1
    elif spends<=200:
        return_money=(spends-100)*0.075+100*0.1
    elif spends<=400:
        return_money=(spends-200)*0.05+100*0.075+100*0.1
    else:
        return_money=(spends-400)*0.03+200*0.05+100*0.075+100*0.1
    print("总优惠金额：",return_money)