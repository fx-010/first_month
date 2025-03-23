import pandas as pd

df = pd.read_csv(r"E:\vscode project\day02\scores.csv")
max_score = df["score"].max()
min_score = df["score"].min()
avg_score = df["score"].mean()

print(f"最高分：{max_score}, 最低分：{min_score}, 平均分：{avg_score}")
with open("score_stats.txt", "w") as f:
    f.write(f"最高分：{max_score}\n最低分：{min_score}\n平均分：{avg_score}")
