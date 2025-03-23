# 导入 Pandas 库
import pandas as pd

# 读取数据
df = pd.read_csv(r"E:\exercise_studying project\day06\scores_day06.csv")

# 打印原始数据，查看初始状态
print("原始数据是:\n",df)

# 任务 1：填充成绩列的缺失值为平均分
# 计算 score 列的平均值（忽略缺失值）
mean_score = df["score"].mean()

# 用 fillna 将缺失值填充为平均值
df["score"] = df["score"].fillna(mean_score)
print("填充(平均数填充)后数据为：\n",df)

# 任务 2：删除重复的学生记录（基于 name 列）
# 使用 drop_duplicates，subset 指定去重的列，keep='first' 保留第一次出现的记录
df = df.drop_duplicates(subset=["name"],keep="first")
print("去除name列中重复的元素并保留第一次出现的记录：\n",df)

# 任务 3：将 class 列中的 "ClassA" 替换为 "A"
# 使用 replace 进行替换
df["class"] = df["class"].replace("ClassA","A")
print("将class列中的ClassA替换为A的数据为：\n",df)

# 保存清洗后的数据到新文件
df.to_csv("cleaned_scores.csv",index=False)

# 最后输出清洗后的数据
print("\n最终清洗的数据为：\n",df)