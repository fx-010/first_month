import pandas as pd
import plotly.express as px# 快速生成图表
import dash
from dash import dcc, html# Dash 的组件库，比如下拉菜单、图表等
from dash.dependencies import Input, Output# 定义交互逻辑（比如选择下拉菜单后更新图表）

df = pd.read_csv(r"E:\exercise_studying project\day24\sales_data.csv")

# 初始化 Dash 应用并设计布局
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Sales Dashboard"),
    # 下拉框
    dcc.Dropdown(
        id="metric-dropdown",
        options=[
            {"label": "Sales", "value": "Sales"},
            {"label": "Profit", "value": "Profit"}
        ],
        value="Sales"
    ),
    # 滑块
    dcc.Slider(
        id="month-slider",
        min=0,
        max=11,
        step=1,
        value=11,
        marks={i: month for i, month in enumerate(df["Month"])}
    ),
    # # 图表区域，名字是 "line-chart"
    dcc.Graph(id="line-chart")
])

# 定义回调函数（交互逻辑）
# 当用户做了某些操作（选择下拉菜单等），Dash会自动调用这个函数来更新页面上的内容（比如图表）
@app.callback(
    Output("line-chart","figure"),
    # 一个回调可以监听多个输入（如下拉菜单 + 滑块），所以输入必须写成列表形式，哪怕只有一个 Input
    [Input("metric-dropdown", "value")]
)
def update_chart(selected_metric):
    fig = px.line(df,x="Month",y=selected_metric,title=f"Monthly{selected_metric}Trend")
    return fig   
# 主函数入口
if __name__ == "__main__":
    app.run(debug=True)