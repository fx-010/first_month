from sklearn import datasets# 提供数据集，比如Iris
from sklearn.model_selection import train_test_split# 拆分训练和测试数据
from sklearn.neighbors import KNeighborsClassifier# KNN分类模型
from sklearn.metrics import classification_report# 评估模型效果
import seaborn as sns# 画好看的图（基于matplotlib）
import matplotlib.pyplot as plt# 基础画图工具

# 加载数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target
# print(iris)

# 拆分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 创建 KNN 分类模型
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)

# 预测与评估模型
y_pred = model.predict(X_test)
print("分类报告:\n", classification_report(y_test, y_pred))

# 可视化分类结果
# hue色调
# [:, 0]:所有行的第0列
# palette是调色板，"Set1"是seaborn内置的一种颜色组合（红蓝绿等鲜艳颜色）
# "o"是圆圈，"s"是正方形，"D"是菱形
sns.scatterplot(x=X_test[:, 0], y=X_test[:, 1], hue=y_pred, palette="Set1", style=y_pred, markers=["o", "s", "D"])
plt.title("KNN Classification Results")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
