weights = list(map(lambda x: int(x), input("请输入学生体重:").split(' ')))
average = sum(weights)/len(weights)
outWeigt = [i for i in weights if i > average]
print('超过平均体重的有:', outWeigt)