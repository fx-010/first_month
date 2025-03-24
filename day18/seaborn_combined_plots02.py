import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv(r"E:\exercise_studying project\day18\sales.csv")

# 创建画布
plt.figure(figsize=(12, 8))

# 第一张图：条形图和折线图组合
plt.subplot(1, 2, 1)
sns.barplot(x="Product", y="Sales", data=df, color='skyblue', label="Sales")  # 条形图
sns.lineplot(x="Product", y="Profit", data=df, color='red', marker='o', label="Profit")  # 折线图
plt.title("Sales vs Profit by Product")
plt.legend()

# 第二张图：散点图与回归线
plt.subplot(1, 2, 2)
sns.scatterplot(x="Sales", y="Profit", data=df)  # 散点图
sns.regplot(x="Sales", y="Profit", data=df, scatter=False, color='blue')  # 只画回归线，不重复散点
plt.title("Sales vs Profit (Regression Line)")

# 调整布局，避免重叠
plt.tight_layout()

# 显示画布
plt.show()