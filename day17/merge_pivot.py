# 数据合并与合并
import pandas as pd

employees = pd.read_csv(r"E:\exercise_studying project\day17\employees.csv")
salaries = pd.read_csv(r"E:\exercise_studying project\day17\salaries.csv")

df = pd.merge(employees, salaries, on="ID")

pivot_table = df.pivot_table(index="Department",values="Salary",aggfunc="mean")

print("合并后的数据：\n", df)
print("\n透视表（部门平均工资）：\n", pivot_table)