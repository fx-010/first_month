import pandas as pd

# 读取csv文件
df = pd.read_csv(r"E:\exercise_studying project\day16\dirty_data.csv")

# 用中位数填充年龄和工资
df['Age'] = df['Age'].fillna(df['Age'].median()) 
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# 去重复值
df.drop_duplicates(inplace=True)

# 格式化工资字段
df['Salary'] = df['Salary'].apply(lambda x: round(x,2))

print("清洗后数据：\n",df)