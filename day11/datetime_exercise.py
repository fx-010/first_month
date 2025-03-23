import pandas as pd
import numpy as np

dates = pd.date_range(start='2024-01-01',end='2024-12-31',freq='D')
sales = np.random.randint(50,200,size=len(dates))
df = pd.DataFrame({'date':dates,'sale':sales})
print('原始数据：\n',df)

# 转化时间索引
df['date'] = pd.to_datetime(df['date'])
df.set_index('date',inplace=True)
print('转化时间索引后数据为：\n',df.head())

# 按月统计销量
monthly_sales = df.resample('M').sum()
print('按月统计销量：\n',monthly_sales)

# 计算七天移动平均
df['moving_avg'] = df['sale'].rolling(window=7).mean()
print("移动平均数据(前10行数据)：",df.head(10))

# 保存处理值
df.to_csv('processed_sales.csv')