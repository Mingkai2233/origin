import os

content = ''
num = '6'
path1 = 'C:\\Users\\Gr4y\\Desktop\\逆向工程\\作业\\班级\\'+num+'\\lec'  # lec目录
path2 = 'C:\\Users\\Gr4y\\Desktop\\逆向工程\\作业\\班级\\'+num+'\\lec'  # lab目录
path3 = 'C:\\Users\\Gr4y\\Desktop\\逆向工程\\作业\\班级\\'+num+'\\作业统计结果.txt'  # 结果文件
file = open(r'C:\Users\Gr4y\Desktop\逆向工程\作业\班级\students.txt', 'r', encoding='UTF-8')
students = dict()  # 学生总名单
data = file.readlines()
for i in data:
    num, name = i.split()
    students[num] = name
file.close()

# 统计lec
data = os.listdir(path1)
total = len(data)
for i in range(total):
    data[i] = data[i][:9]
res = set(students.keys()) - set(data)  # 没交人的学号
content = content + 'lec 未交人数: ' + str(len(res)) + '\n名单:\n'
for i in res:
    content = content + i + ' ' + students[i] + '\n'
# 统计lab
data = os.listdir(path2)
total = len(data)
for i in range(total):
    data[i] = data[i][:9]
res = set(students.keys()) - set(data)  # 没交人的学号
content = content + '\n\nlab 未交人数: ' + str(len(res)) + '\n名单:\n'
for i in res:
    content = content + i + ' ' + students[i] + '\n'
file = open(path3, 'w')
file.write(content)
print("统计完成")
