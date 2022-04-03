import random
file = open("weakcode.txt", 'r')
message = ['huawei', 'admin']
symbol = '!@#$%^&*~'
weakcode = None
weakcode = file.readlines()
file.close()
weakcode = list(map(lambda x: x[:-1], weakcode))
# input message
# message.append(input("名字:"))
# message.append(input("名字缩写:"))
# message.append(input("身份证号:"))
file = open('codes.txt', 'w+')
for i in range(len(message)):
    for j in range(len(symbol)):
        for k in range(len(weakcode)):
            file.write(message[i]+symbol[j]+weakcode[k]+'\n')
print('successfully')
file.close()