# 问题描述:
# 给定一个数N, start > 1, end < N, 要求输出机器人行走k步从开始到结束点的路径数量


# 暴力递归版本
def force(n: int, k: int, start: int, end: int):
    return process1(n, start, end, k, start)


def process1(n, start: int, end: int, rest: int, curp: int):
    if rest == 0:
        return 1 if curp == end else 0
    if curp == 0:
        return process1(n, start, end, rest-1, curp + 1)
    elif curp == n:
        return process1(n, start, end, rest-1, curp - 1)
    else:
        return process1(n, start, end, rest-1, curp + 1) + process1(n, start, end, rest, curp - 1)


# 记忆化搜索
def memorySearch(n, k, start, end):
    memory = [[-1 for i in range(n+1)] for i in range(k+1)]
    ans = process2(n, end, k, start, memory)
    return ans


def process2(n, end, rest, curp, memory):
    if memory[rest][curp] != -1:
        return memory[rest][curp]
    if rest == 0:
        memory[rest][curp] = 1 if curp == end else 0
        return memory[rest][curp]
    if curp == 0:
        memory[rest][curp] = process2(n, end, rest - 1, curp + 1, memory)
    elif curp == n:
        memory[rest][curp] = process2(n, end, rest - 1, curp - 1, memory)
    else:
        memory[rest][curp] = process2(n, end, rest - 1, curp - 1, memory) + process2(n, end, rest - 1, curp + 1, memory)
    return memory[rest][curp]


if __name__ == '__main__':
    print(force(10, 4, 2, 4))
    print(memorySearch(10,4,2,4))


