import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"E:\exercise_studying project\day14\sales.csv")

# 折线图
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Sales"], marker='o', linestyle='-', color='b', label="Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.legend()
plt.show()

# 柱状图
plt.figure(figsize=(8, 5))
plt.bar(df["Month"], df["Sales"], color='g')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Bar Chart")
plt.show()