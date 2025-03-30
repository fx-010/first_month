import pandas as pd
import plotly.express as px

# 绘制交互式折线图
# px.line：用plotly.express的line功能画一条折线图，显示数据随时间变化的趋势
df = pd.read_csv(r"E:\exercise_studying project\day21\sales_interactive.csv")
fig1 = px.line(df, x="Month", y="Sales", title="Monthly Sales Trend", markers=True)# markers=True：在折线上显示小点
fig1.show()

# 绘制交互式散点图
# size:点的大小根据 "Profit" 列的值变化，利润越大，点越大
# hover_data=["Month"]：当鼠标悬停在点上时，会额外显示 "Month" 的值
fig2 = px.scatter(df, x="Sales", y="Profit", color="Month",title="Sales vs Profit", size="Profit", hover_data=["Month"])
fig2.show()