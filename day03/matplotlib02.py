import matplotlib.pyplot  as plt 
import random

#修改字体避免中文字不显示问题
plt.rcParams['font.sans-serif']  = ['SimHei']
plt.rcParams['axes.unicode_minus']  = False  

x = range(50)
y_yueyang = [random.uniform(20,35) for i in x]
y_beijing = [random.uniform(10,25) for i in x]
plt.figure(figsize=(10,10),dpi=100)#大小及分辨率

#画出两个城市
plt.plot(x,y_yueyang,linestyle="--",label="岳阳")
plt.plot(x,y_beijing,linestyle=":",label="北京")

plt.legend(loc='upper right')#图例位置
x_lable = ['11点{}分'.format(i) for i in x]
plt.xticks(x[::5],x_lable[::5])
plt.yticks(range(0,40,5))

plt.grid(True)#画出刻度
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("岳阳-北京城市温度变化")
plt.savefig("day03.jpg")
plt.show()