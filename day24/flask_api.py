from flask import Flask,request,jsonify
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)# __name__ 是 Python 的内置变量，表示当前文件
df = pd.read_csv(r"E:\exercise_studying project\day24\titanic.csv")

df["Sex"] = df["Sex"].map({"male":1,"female":0})# 机器学习只能处理数字
X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]].copy()# 加.copy()明确创建副本，避免警告
y = df["Survived"]

X.fillna(X.mean(),inplace=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# 创建逻辑回归模型，并用训练集数据训练
model = LogisticRegression()
model.fit(X_train,y_train)

@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json()
    input_data = pd.DataFrame([data])
    input_data.fillna(X.mean(),inplace=True)
    prediction = model.predict(input_data)[0]
    return jsonify({"Survived":int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)

# Pclass：舱位等级（1 = 一等舱，2 = 二等舱，3 = 三等舱）
# Sex：性别（你的代码中 male=1，female=0）
# Age：年龄（乘客的年龄，单位是年，可以是小数）
# SibSp：兄弟姐妹/配偶数量（同行的人数）
# Parch：父母/子女数量（同行的人数）
# Fare：票价（单位是当时的英镑，可以是小数）
