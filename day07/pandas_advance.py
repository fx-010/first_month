import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv(r"E:\exercise_studying project\day07\scores_day07.csv")
print(f"原始数据：\n{df}\n格式：\n{df.dtypes}")

# 将名字字母大写
df["name"] = df["name"].str.upper()
print(df)

# 将“score”行转化为浮点型
df["score"] = df["score"].astype(float)
print(df)

# 分组并统计每个班的平均成绩
class_avg = df.groupby("class")["score"].mean()
print(f"每个班的平均成绩是：\n{class_avg}分")

# 将计算出来的每个票平均值按class值保存到'pandas_advance.csv'的新的一列中去
# df["class"]是一个Series对象，是根据某种映射关系传入参数而不是字符串"'class_avg'"
df["class_avg"] = df["class"].map(class_avg)

df.to_csv("pandas_advance.csv",index=False)