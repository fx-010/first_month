import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv(r"E:\exercise_studying project\day23\titanic.csv")

df["Sex"]=df["Sex"].map({"male":1,"female":0})

X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]]
y = df["Survived"]

# 处理空值
X.fillna(X.mean(),inplace=True)

# 分两部分(训练和测试)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# 让模型学习
model = LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

# 预测和检查
y_pre = model.predict(X_test)
accuracy_score(y_test,y_pre)

print("预测正确率:", accuracy_score(y_test, y_pre))