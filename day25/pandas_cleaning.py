import pandas as pd
df = pd.read_csv(r"E:\first_month\day25\customer_data.csv")

# 处理缺失值
df["Age"] = df["Age"].fillna(df["Age"].median())  # 用中位数填充年龄
df["PurchaseAmount"] = df["PurchaseAmount"].fillna(df["PurchaseAmount"].mean())  # 用均值填充消费金额
df["JoinDate"] = df["JoinDate"].fillna("Unknown")  # 缺失日期填充"Unknown"

# 重复值
df.drop_duplicates(inplace=True)
# 格式转换
df["PurchaseAmount"] = df["PurchaseAmount"].astype(float)

# errors 参数：
# 控制 pd.to_datetime() 在遇到无法解析的日期字符串时的行为
# 可选值包括：
# 'raise'（默认）：遇到无效值时抛出异常，程序停止
# 'coerce'：将无效值强制转换为 NaT（Not a Time，Pandas 中的缺失时间值），程序继续运行
# 'ignore'：忽略错误，返回原始输入值（不转换）
df["JoinDate"] = pd.to_datetime(df["JoinDate"],errors='coerce')

df.to_csv("cleaned_customer_data.csv", index=False)
print("数据清洗完成，已保存到 cleaned_customer_data.csv")
