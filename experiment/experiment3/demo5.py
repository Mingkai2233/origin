def func(string):
    length = len(string)
    end = 1 << length  # 获得字串的个数
    result = []
    for i in range(end):
        array = []  # 存储当前子串
        for j in range(length):
            if (i >> j) % 2:
                array.append(string[j])
        result.append(array)
    print(result[1:])  # 输出空串以外的子串

string = list(input())
func(string)
