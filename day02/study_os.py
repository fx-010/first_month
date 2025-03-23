import os
folder_path = r"C:\Users\Lenovo\Desktop\make_folder"
files = os.listdir(folder_path)
with open("file_list.txt", "w") as f:
    f.write("文件夹内容：" + str(files))
print("文件列表已保存")