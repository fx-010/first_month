import pandas as pd
import matplotlib.pyplot as plt
# 从scikit-learn（一个机器学习库）的linear_model模块中导入LinearRegression类
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"E:\exercise_studying project\day21\house_prices.csv")
# scikit-learn要求特征是表格形式（即使只有一列）,而不是单个列表
X = df[['Area']]  # 作为模型的特征（输入）
y = df['Price']   # 模型的目标（输出）

# 创建一个线性回归模型的实例
model = LinearRegression()
model.fit(X,y)# fit方法根据数据计算出一条最佳的直线，让这条直线尽量贴近所有的数据点

# 模型预测
# predict方法用模型学到的直线方程，计算每个面积(X)对应的预测价格(y)
df['Predicted_Price'] = model.predict(X)

# 可视化
plt.scatter(df['Area'], df['Price'], color='blue', label='Actual Price')
plt.plot(df['Area'],df['Predicted_Price'],color='red',label='Predicted Price')
plt.xlabel('Area (sqft)')
plt.ylabel('Price ($)')
plt.title('House Price Prediction')
plt.legend()
plt.show()