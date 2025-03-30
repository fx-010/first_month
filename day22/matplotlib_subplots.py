import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\exercise_studying project\day22\sales.csv")

# 创建子图
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# 子图1：销售趋势折线图
axs[0, 0].plot(df['Month'], df['Sales'], marker='o', color='b')
axs[0, 0].set_title("Sales Trend")
axs[0, 0].set_xlabel("Month")
axs[0, 0].set_ylabel("Sales ($)")
axs[0, 0].tick_params(axis='x', rotation=45)  # 旋转 x 轴标签，度数45°
axs[0, 0].grid(True, linestyle='--', alpha=0.7)# 网格线，透明度

# 子图2：利润趋势折线图
axs[0, 1].plot(df['Month'], df['Profit'], marker='o', color='r')
axs[0, 1].set_title("Profit Trend")
axs[0, 1].set_xlabel("Month")
axs[0, 1].set_ylabel("Profit ($)")
axs[0, 1].tick_params(axis='x', rotation=45)
axs[0, 1].grid(True, linestyle='--', alpha=0.7)

# 子图3：销售和利润柱状图（并排显示）
bar_width = 0.4
x = range(len(df['Month']))
# [i - bar_width/2 for i in x] 计算每个柱子的位置(列表推导式)：计算销售柱子的中心位置，向左偏移半个柱子宽度
axs[1, 0].bar([i - bar_width/2 for i in x], df['Sales'], bar_width, color='g', alpha=0.7, label='Sales')
axs[1, 0].bar([i + bar_width/2 for i in x], df['Profit'], bar_width, color='y', alpha=0.7, label='Profit')
axs[1, 0].set_title("Sales vs Profit")
axs[1, 0].set_xlabel("Month")
axs[1, 0].set_ylabel("Amount ($)")
axs[1, 0].set_xticks(x)
axs[1, 0].set_xticklabels(df['Month'], rotation=45)
axs[1, 0].legend()  # 添加图例
axs[1, 0].grid(True, linestyle='--', alpha=0.7)

# 子图 4：销售和利润对比散点图
axs[1, 1].scatter(df['Sales'], df['Profit'], color='purple')
axs[1, 1].set_title("Sales vs Profit Scatter")
axs[1, 1].set_xlabel("Sales ($)")
axs[1, 1].set_ylabel("Profit ($)")
axs[1, 1].grid(True, linestyle='--', alpha=0.7)

# 美化布局并显示
plt.tight_layout()# 自动解决布局问题，避免与相邻子图冲突
plt.show()
