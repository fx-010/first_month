import json

# 读取TXT文件
with open(r"E:\exercise_studying project\day15\students.txt","r",encoding="utf-8") as file:
    # readlines方法将文件的每一行读取为列表的一个元素
    lines = file.readlines()
    # strip 方法去除首尾空格，并按逗号分割（split(",")）
    students = [line.strip().split(",") for line in lines] 
print("学生数据:",students)

# 读取JSON文件
with open(r"E:\exercise_studying project\day15\students.json","r",encoding="utf-8") as file:
    students_json = json.load(file)
print("json文件数据：",students_json)

# 将TXT文件转化为JSON文件并保存；"name": s[0]：将[0]的字符映射到键‘name’上
students_list = [{"name": s[0], "age": int(s[1]), "department": s[2]} for s in students]
with open("converted_students.json", "w", encoding="utf-8") as file:
    # JSON提供的函数，将Python数据结构(列表，字典等)转化为JSON数据;"file"是文件对象不是文件名
    json.dump(students_list, file, indent=4)

print("已将 TXT 数据转换为 JSON 并保存！")