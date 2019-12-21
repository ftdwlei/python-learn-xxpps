# 输出姓名和成绩
# author：captain
score=[80,70,90]
min_grade=None
max_grade=None
sum_grade=0.0

print("我的名字是：小小。")
print("本次考试我的语文成绩是：%d"%score[0])
print("           数学成绩是：%d"%score[1])
print("           英语成绩是：%d"%score[2])

sum_grade=score[0]+score[1]+score[2]
avg_grade=sum_grade/3
print(min(score))
min_grade=score.index(min(score))
max_grade=score.index(max(score))
print("总分：",sum_grade)
print("最高分：",score[max_grade])
print("最低分：",score[min_grade])
print("平均分：",avg_grade)