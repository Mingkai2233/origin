list1 = list(map(int, input("请输入一串数字").split(",")))
result1 = [i for i in list1 if i % 2 == 0]
print(result1)