import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv(r"E:\exercise_studying project\day16\employee_data.csv")

# 绘制小提琴图（各部门工资分布）
plt.figure(figsize=(8, 5))
plt.subplot(1,2,1)
sns.violinplot(x="Department", y="Salary",data=df)
plt.title("Salary Distribution by Department (Violin Plot)")

# 使用pivot_table创建一个数据透视表
# 行列分别对应的是Department和Salary的数值agg处理values的值的方法
salary_matrix = df.pivot_table(index="Department",values="Salary",aggfunc="mean")

# 绘制热力图（Department和Salary间的关系） 
# annot：(annotation)注解;fmt:(format)格式;
# cmap(colormap);YlGnBu:(yellow,green,blue)
plt.subplot(1,2,2)
sns.heatmap(salary_matrix,  annot=True, fmt=".2f", cmap="YlGnBu") 
plt.title("Average  Salary by Department (Heatmap)") 

plt.show()  