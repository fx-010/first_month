import pandas as pd

df = pd.read_csv(r"E:\exercise_studying project\day23\sales_data.csv")

pivot_table = df.pivot_table(index="Region", columns="Month", values="Sales", aggfunc="sum")
print("数据透视表：\n", pivot_table)

# 创建交叉表
cross_table = pd.crosstab(df["Region"], df["Product"])
print("交叉表：\n", cross_table)
