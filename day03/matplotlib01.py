import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("day03/scores_day03.csv")#读取该路径上的csv文件
class_avg = df.groupby("class")["score"].mean()#求平均值
class_avg.plot(kind="bar")
plt.title("Class Average Scores")#标题

#xy轴的标注
plt.xlabel("Class")
plt.ylabel("Average Score")
plt.savefig("day03.jpg")#保存
plt.show()