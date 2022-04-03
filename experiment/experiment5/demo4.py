import pickle


def is_perfect_num(num: int) -> bool:  # 判断一个数是否为完全数
    nums = []
    for i in range(1, num):
        if num % i == 0:
            nums.append(i)
    if sum(nums) == num:
        return True
    else:
        return False


if __name__ == '__main__':
    m = int(input("请输入范围上限m:"))
    result = []
    for i in range(2, m+1):
        tmp = []
        if is_perfect_num(i): # 如果是完全数就寻找他的所有真因子
            tmp.append(i)
            for j in range(1, i-1):
                if i % j == 0:
                    tmp.append(j)
            result.append(tmp)

    file = open('result.dat', 'bw')  # 以二进制写的方式打开
    pickle.dump(result, file)  # 对象序列化写入
    del result
    file.close()

    file = open('result.dat', 'rb')  # 以二进制读的方式打开
    result = pickle.load(file)  # 对象反序列化读出
    print(result)

