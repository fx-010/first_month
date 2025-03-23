import pandas as pd

# 读取 CSV 文件
df = pd.read_csv(r"E:\exercise_studying project\day15\dirty_data.csv")

# 处理缺失值（用均值填充）
# Pandas 3.0 将弃用链式赋值（df["列名"].method(inplace=True)）
df = df.fillna({"Salary":  df["Salary"].mean()})

# 删除重复(行)数据
# 直接在原DataFrame上修改
df.drop_duplicates(inplace=True)

# 统计部门平均工资(分组，对薪资列求平均值)
avg_salary = df.groupby("Department")["Salary"].mean()

print("清洗后的数据:\n", df)
print("\n各部门平均工资:\n", avg_salary)