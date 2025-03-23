import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"E:\exercise_studying project\day17\department_salaries.csv")

# 绘制堆叠条形图（按部门统计工资分布）
# hue指定按 "Salary"（薪水）进行颜色区分
# multiple="stack"指定当有多个hue类别时，如何堆叠柱子
# bins指定直方图的分桶数量
plt.figure(figsize=(8,5))
sns.histplot(data=df, x="Department", hue="Salary", multiple="stack", bins=5)
plt.title("Salary Distribution by Department (Stacked)")
plt.show

# 绘制散点图（部门 vs 工资）
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="Department", y="Salary", hue="Department", size="Salary")
plt.title("Scatter Plot of Salary by Department")
plt.show()