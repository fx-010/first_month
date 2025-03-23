import pandas as pd
df = pd.read_csv(r"E:\exercise_studying project\day05\scores_day05.csv")
print("原始数据：\n",df.head())

filtered = df[(df["score"]>80)&(df["class"]=="A")]
print(f"大于80分且是A班的学生有{filtered}")

#添加index防止多出一列索引
filtered.to_csv("filtered05_csv",index=False)