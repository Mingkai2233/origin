# n, total = map(int, input().split())
# nums = list(range(1, n+1))
# total_2 = sum(nums)
# for i in range(1, n):
#     index = False
#     for j in range(i+1, n+1):
#         if (total_2-i-j)*(n-1)+i+j == total:
#             left = i
#             right = j
#             index = True
#             break
#     if index:
#         break
# res = [0 for k in range(n)]
# if not(str(left) < str(right)):
#     left, right = right, left
# res[0] = left
# res[n-1] = right
# i = 1
# for num in nums:
#     if num != left and num != right:
#         res[i] = num
#         i+=1
# for num in res:
#     print(num, end=" ")
import itertools
import random


def productTest(nums):
    length = len(nums)
    n = length-1
    for i in range(n):
        for j in range(length-1-i):
            nums[j] = nums[j]+nums[j+1]
    return nums[0]


if __name__ == '__main__':
    n, total = map(int, input().split())
    base = list(range(1, n+1))
    base = itertools.permutations(base)
    permutation = base
    index = False
    for p in permutation:
        if productTest(list(p)) == total:
            index = True
            break
    if index:
        for i in p:
            print(i, end=' ')


