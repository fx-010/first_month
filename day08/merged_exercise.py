import pandas as pd

students = pd.read_csv(r"E:\exercise_studying project\day08\students_day08.csv")
scores = pd.read_csv(r"E:\exercise_studying project\day08\scores_day08.csv")

merged = pd.merge(students,scores,on="student_id",how="inner")
print(merged)
class_avg = merged.groupby("class")["score"].mean()
print(class_avg)

merged.to_csv("merged_data.csv",index=False)