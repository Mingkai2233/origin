file = open('test11.txt', 'r', encoding='UTF-8')
context = file.read()
num1 = 0
num2 = 0
num1 = context.count('其')
num2 = context.count('，') + context.count('。') + context.count('？') +\
       context.count('“') + context.count('：') + context.count('”')
print("文件内容为：\n", context)
print("\n其字的个数为：", num1)
print("标点符号的个数:", num2)