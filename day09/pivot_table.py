import pandas as pd
df = pd.read_csv(r"E:\exercise_studying project\day09\merged_data_day09.csv")
print('原始数据：\n',pd)

# 创建数据透视表
pivot = pd.pivot_table(df,
                       values="score",
                       index="class",
                       columns="gender",
                       aggfunc="mean")
print("按班级和性别统计的平均成绩：\n",pivot)

# 创建数据透视表，添加总计
pivot_with_sum = pd.pivot_table(df,
                       values="score",
                       index="class",
                       columns="gender",
                       aggfunc="mean",
                       margins=True,
                       margins_name='Total')
print("按班级和性别统计的平均成绩(含总计)：\n",pivot_with_sum)