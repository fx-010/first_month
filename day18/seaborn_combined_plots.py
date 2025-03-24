import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\exercise_studying project\day18\sales.csv")

plt.figure(figsize=(10,6))

sns.barplot(x="Product", y="Sales", data=df, color='skyblue', label="Sales")# 条形图
sns.lineplot(x="Product", y="Profit", data=df, color='red', marker='o', label="Profit")# 折线图
plt.title("Sales vs Profit by Product")
# 图例
plt.legend()
plt.show()

# 创建散点图与回归线（查看销售与利润的关系）
sns.lmplot(data=df,x="Sales",y="Profit")
plt.title("Sales vs Profit (Regression Line)")
plt.show()