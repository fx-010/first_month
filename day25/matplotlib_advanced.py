import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100) # 生成从 0 到 10 的 100 个均匀分布的数字，作为 x 轴数据
y1 = np.sin(x) #v 计算 x 的正弦值，生成波浪形的数据（范围在 -1 到 1）
y2 = np.cos(x) # 计算 x 的余弦值，同样是波浪形，但与正弦波错开

# 多子图
fig,axs = plt.subplots(2,1,figsize=(8,6))
axs[0].plot(x, y1, label="Sine Wave", color="blue")
axs[1].plot(x, y2, label="Cosine Wave", color="red")

# 双坐标绘制
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y1, "g-", label="Sine")
ax2.plot(x, y2, "b--", label="Cosine")

# 动态绘制
plt.ion()
for i in range(len(x)):
    plt.clf()
    plt.plot(x[:i],y1[:i],"r-")
    plt.pause(0.05)
plt.ioff()

plt.show()
