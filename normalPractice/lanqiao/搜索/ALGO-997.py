def my_max(nums):
    tmp = [i for i in nums if i != 0]
    return max(tmp)


def my_min(nums):
    tmp = [i for i in nums if i != 0]
    return min(tmp)


def process(sticklen, num, m):
    res = my_max(sticklen) - my_min(sticklen)
    if num == m:
        return res
    for i in range(len(sticklen)):
        for j in range(i+1, len(sticklen)):
            if sticklen[i] != 0 and sticklen[j] != 0:
                tmp = sticklen[i]
                sticklen[j] += sticklen[i]
                sticklen[i] = 0
                res = min(res, process(sticklen, num-1, m))
                sticklen[i] = tmp
                sticklen[j] -= tmp
    return res


if __name__ == "__main__":
    n ,m= map(int, input().split())
    sticklen = list(map(int, input().split()))
    print(process(sticklen, n, m))
