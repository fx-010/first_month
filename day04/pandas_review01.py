import pandas as pd

# 读取数据
df = pd.read_csv("E:\exercise_studying project\day04\scores_day04.csv")
print('原始数据：\n',df)

# 按成绩排序，输出前5名(降序)
top5 = df.sort_values(by="score",ascending=False).head(5)
print(f"成绩前五名是:\n{top5}")

# 筛选操作：成绩大于 90 的学生
high_scores = df[df['score']>90]
print("成绩大于90分的学生：\n",high_scores)

# 分组操作：按班级计算平均成绩
class_avg = df.groupby('class')['score'].mean()
print("按班级计算平均分的结果是：\n",class_avg)

# 统计操作：计算最高分、最低分和平均分
max_score = df["score"].max()
min_score = df["score"].min()
avg_score = df["score"].mean()
print(f"最高分是{max_score}\n最低分是{min_score}\n平均分是{avg_score:.6f}")

# 综合练习：筛选成绩前5名中 A 班的学生
top5_A_class = df.sort_values(by="score",ascending=False).head(5)
top5_A_class = top5_A_class[top5_A_class["class"] == "A"]
print(f"前五名中的A班学生是：{top5_A_class}")