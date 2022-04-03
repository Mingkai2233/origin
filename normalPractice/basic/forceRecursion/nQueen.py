# 一般解法
def nQueen(n: int):
    limit = [-1 for i in range(n)]
    result = process(0, limit, n)
    print(result)


def process(i: int, limit: list, n: int) -> int:  # limit记录的是第n个皇后在第几列放着
    if i == n:
        return 1
    res = 0
    for j in range(n):
        if isValid(i, j, limit):
            limit[i] = j
            res += process(i+1, limit, n)
    return res


def isValid(i: int, j: int, limit) -> bool:
    for t in range(i):
        if limit[t] == j or abs(i-t) == abs(j-limit[t]):
            return False
    return True


# 经过位运算提速的解法
def nQueenPro(n: int):
    num = 2**n - 1



def processPro(i: int, limit: int, n: int ):
    pass


if __name__ == "__main__":
    nQueen(4)