import pandas as pd
df = pd.read_csv(r"E:\exercise_studying project\day09\merged_data_day09.csv")
pivot = pd.pivot_table(df,values='score',index='class',aggfunc=['max','min'])
print('最高和最低成绩为：\n',pivot)