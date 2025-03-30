import pandas as pd

df = pd.read_csv(r"E:\exercise_studying project\day20\sales_data.csv")

# 透视表（查看每种类别的总销售额）
pivot = df.pivot_table(values="Sales", index="Category", aggfunc="sum")
print("透视表：\n", pivot)

# 分组聚合（计算每种产品的平均利润）
grouped = df.groupby("Product")["Profit"].mean()
print("产品平均利润：\n", grouped)

# 计算累计销售额,".sum()"是求总和返回一个结果
df["Cumulative Sales"] = df["Sales"].cumsum()# ".cumsum()"结果是逐行递增的序列
print("累计销售额：\n", df)
