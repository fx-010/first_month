import pandas as pd

orders = pd.read_csv(r"E:\exercise_studying project\day22\orders.csv")
products = pd.read_csv(r"E:\exercise_studying project\day22\products.csv")

merged_df = pd.merge(orders,products,on="ProductID")

merged_df["total_price"] = merged_df["Quantity"]*merged_df["Price"]
product_sales = merged_df.groupby('ProductName')["total_price"].sum().reset_index()# 将旧索引添加为列，并使用新的顺序索引

print("合并后的数据：\n", merged_df)
print("\n每个产品的总销售额：\n", product_sales)