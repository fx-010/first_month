#os.listdir()遍历文件夹中的文件
#os.path.join()拼接文件路径
#os.rename()重命名文件

import os
folder_path = r"C:\Users\Lenovo\Desktop\make_folder"#绝对路径
for filename in os.listdir(folder_path):
    new_filename = "backup_" + filename#拼接
    os.rename(
        os.path.join(folder_path, filename),#旧路径
        os.path.join(folder_path, new_filename)#新路径
    )

#判断路径是否已经存在该文件
if os.path.exists(folder_path):
    print("文件已经存在，并重命名！")
else:
    os.mkdir(folder_path)
    print("已成功创建并重命名！",folder_path)