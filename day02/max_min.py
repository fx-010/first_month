num_start = []
for i in range(5):
    num = float(input(f'请输入第{i+1}个数:'))
    num_start.append(num) 
print('最大值:', max(num_start))
print('最小值:', min(num_start))
 
with open('result01.txt','w') as f:
    f.write(f"最大值{max(num_start)}\n平均值{sum(num_start)/len(num_start):.2f}")