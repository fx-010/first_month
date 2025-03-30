import pandas as pd

df = pd.read_csv(r"E:\exercise_studying project\day19\dirty_data.csv")

df["Age"] = df["Age"].fillna(df["Age"].mean())# 均值填充
df["Salary"] = df["Salary"].fillna(df["Salary"].median())# 中位数

df.drop_duplicates(inplace=True)# 去重

df["JoinDate"] = pd.to_datetime(df["JoinDate"])# 转化数据类型

df = df[df["Salary"]<10000]# 只取<10000的，大于10000视为异常

print("清理后的数据：\n", df)