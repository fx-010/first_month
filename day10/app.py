from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def show_quotes():
    df = pd.read_csv(r"E:\exercise_studying project\quotes_with_authors.csv")
    return render_template("index.html", data=df.to_dict("records"))# 按行转化为列表，其中列表的每个元素是一个字典

if __name__ == "__main__":
    app.run(debug=True)