import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为 SimHei
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示为方框的问题

df = pd.read_csv(r"E:\exercise_studying project\day20\sales_data.csv")

# 直方图(histogram)（销售额分布）
plt.hist(df["Sales"],bins=5,color="blue",alpha=0.7)
plt.title("销售额分布")
plt.xlabel("销售额")
plt.ylabel("频数")
plt.show()

# 双轴图(dual-axis plot)（销售额 vs. 利润）
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()# 共享X轴，独立的Y轴
ax1.bar(df["Product"], df["Sales"], color="blue", label="销售额")
ax2.plot(df["Product"], df["Profit"], color="red", marker="o", label="利润")
ax1.set_ylabel("销售额")
ax2.set_ylabel("利润")
plt.title("销售额与利润对比")
plt.show()

# 折线图（累计销售额趋势）
df["Cumulative Sales"] = df["Sales"].cumsum()
plt.plot(df["Date"],df["Cumulative Sales"],marker="o", linestyle="-", color="green")
plt.xticks(rotation=45)# 调整轴刻度（tick）和刻度标签（tick label）
plt.title("累计销售额趋势")
plt.xlabel("日期")
plt.ylabel("累计销售额")
plt.show()
