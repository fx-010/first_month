import pandas as pd

df = pd.read_csv(r"E:\exercise_studying project\day16\sales_data.csv")

# 按类别汇总销售额
category_sales = df.groupby("Category")["Amount"].sum()

# 计算每个产品的销售比率
# 销售比率:每个产品的销售额占总销售额的比例
total_sales = df["Amount"].sum()
df["Sales_Ratio"] = df["Amount"]/total_sales
print('销售比率为：\n',df)