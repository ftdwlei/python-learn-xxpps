# 比较和逻辑，判断等腰、等边、直角三角形
# author：captain

a=int(input("输入三角形的边长a："))
b=int(input("输入三角形的边长b："))
c=int(input("输入三角形的边长c："))
if a<=0 or b<=0 or c<=0:
    print("worng input!")
elif (a+b)>c and (a+c)>b and (b+c)>a:
    print("可以组成三角形")
    if a==b==c:
        print("等边三角形")
    elif a==b or b==c or a==c:
        print("等腰三角形")
    if (a*a+b*b)==c*c or (a*a+c*c)==b*b or (c*c+b*b)==a*a:
        print("直角三角形")
