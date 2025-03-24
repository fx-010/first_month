import pandas as pd

orders = pd.read_csv(r"E:\exercise_studying project\day18\orders.csv")
products = pd.read_csv(r"E:\exercise_studying project\day18\products.csv")

merged_df = pd.merge(orders,products,on='ProductID')

# 计算每个订单的总价
merged_df["TotalPrice"] = merged_df["Quantity"] * merged_df["Price"]

# 按ProductName分组并计算每个产品的总销售额
# .reset_index()“重置索引”，把索引变成列，用默认整数索引替代
product_sales = merged_df.groupby("ProductName")["TotalPrice"].sum().reset_index()

# 输出合并后的数据和销售统计
print("合并后的数据：\n", merged_df)
print("\n每个产品的总销售额：\n", product_sales)