import pandas as pd
df = pd.read_csv(r"E:\exercise_studying project\day10\merged_data_day10.csv")
print('原始数据是：\n',df)
# 按班级和性别统计平均成绩
pivot = pd.pivot_table(df,
                       values='score',
                       index=['class'],
                       columns=['gender'],
                       aggfunc='mean',
                       fill_value=0)
# 保留两位小数
pivot = pivot.round(2)

print("按照班级和性别统计成绩的数据(缺失值用0填充,保留两位小数):\n",pivot)
pivot.to_csv('pivot_table_res.csv')
print('已保存为pivot_table_res.csv成功！')