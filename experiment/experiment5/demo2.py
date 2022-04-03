file1 = open('test22.txt', 'r', encoding='UTF-8')
context1 = file1.readlines()
file1.close()
file1 = open('test22.txt', 'w')
numOfLine = len(context1)
for i in range(numOfLine):
    if len(context1[i]) != 1:
        context1[i] = context1[i][3:]
    print(context1[i], end='')
    file1.write(context1[i])
file1.close()