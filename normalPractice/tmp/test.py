def climbStairs(n: int) -> int:
    return process(0, n)


def process(i: int, n: int) -> int:
    if i == n:
        return 1
    if i > n:
        return 0
    return process(i + 1, n) + process(i + 2, n)

print(climbStairs(5))