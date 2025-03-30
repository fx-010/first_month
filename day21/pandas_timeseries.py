import pandas as pd

df = pd.read_csv(r"E:\exercise_studying project\day21\stock_data.csv")

# 数据合并：模拟多个股票数据的合并
# 简单使用pivot_table将数据重塑
pivot_df = df.pivot_table(index='Date',columns='Stock',values='Price')
print("透视表数据：\n", pivot_df)

# 计算AAPL的7日滚动均值（示例滚动窗口设置为2）
pivot_df["AAPL_Rolling"] = pivot_df['AAPL'].rolling(window=2).mean()
print("\nAAPL滚动均值：\n", pivot_df)