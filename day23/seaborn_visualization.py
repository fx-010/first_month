import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为 SimHei
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示为方框的问题

df = pd.DataFrame({
    "Category": np.random.choice(["A", "B", "C","D"], size=100),
    "Value": np.random.randint(10, 50, size=100)
})

# 画箱型图
plt.figure(figsize=(8, 6)) 
sns.boxplot(x="Category", y="Value", data=df) 
plt.title("箱型图")  # 设置标题
plt.show() 

# 画热图
# "size": 计算每个组合的出现次数（行数）
heatmap_data = pd.pivot_table(df, index="Category", columns="Value", aggfunc="size", fill_value=0)
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, annot=False, cmap="coolwarm")  # annot=False 因为值太多，不显示每个格子的具体数值
plt.title("热图示例 - 每个类别值的计数")
plt.xlabel("数值")
plt.ylabel("类别")
plt.show()