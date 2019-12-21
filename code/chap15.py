# 字典制作通讯录
# author:captain

dict1={'妞妞':'2200 Mission College Blvd,Santa Clara, CA 95054','小花':'2054 Hamilton Ave, San Jose, CAeBay','石头':'100 Winchester Circle, Los Gatos, CA 95032','小丁':'1065 La Avenida Street, Mountain View, CA 94043'}
while 1:
    print(dict1)
    choice = int(input("请选择要做的操作：【1】添加 【2】修改 【3】删除 【0】退出"))
    if choice == 1:
        name = input("新增姓名:")
        addr = input("住址：")
        dict1[name] = addr
        print("已添加")
    elif choice == 2:
        name = input("姓名(请勿写错):")
        if dict1.get(name):
            print("%s原地址是%s", name, dict1[name])
            addr = input("请输入新地址：")
            dict1[name] = addr
        else:
            print("wrong name!")
    elif choice == 3:
        name = input("姓名(请勿写错):")
        if dict1.get(name):
            dict1.pop(name)
            print("已删除")
        else:
            print("wrong name!")
    elif choice==0:
        print(dict1)
        break;
    else:
        print("wrong input!,try again!")