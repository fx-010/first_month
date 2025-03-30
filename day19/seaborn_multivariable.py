import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\exercise_studying project\day19\sales_extended.csv")

# 成对关系图pairplot
sns.pairplot(df, hue="Category")
plt.show()

# sns.FacetGrid(数据, 分割依据(这里'column'是'列'的意思), 大小参数)
g = sns.FacetGrid(df, col="Category", height=4, aspect=1)# 准备了一个"子图"画布;aspect:宽高比

# sns.scatterplot:Seaborn的一个函数，用来画散点图
g.map_dataframe(sns.scatterplot, x="Sales", y="Profit")
plt.show()