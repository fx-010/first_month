import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\exercise_studying project\day15\employees.csv")

# 创建一个图形窗口
plt.figure(figsize=(12, 5))

# 第一个子图：箱型图
# 1行2列，第1个位置
plt.subplot(1, 2, 1)
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary Distribution by Department")

# 第二个子图：散点图
# 1行2列，第2个位置
plt.subplot(1, 2, 2)
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Age vs Salary")

plt.show()