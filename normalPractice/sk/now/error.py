# n = int(input())
# nums = list(map(int, input().split()))
# res = [0 for i in range(len(nums))]
# i = 1
# while i < len(nums):
#     if nums[i] > nums[i-1]:
#         while nums[i] > nums[i-1]+2:
#             nums[i] -= 1
#             nums[i-1] += 1
#             res[i] -= 1
#             res[i-1] += 1
#         nums[i] -= 1
#         res[i] -= 1
#     elif nums[i] == nums[i-1]:
#         nums[i] += 1
#         res[i] += 1
#     else:
#         tmp = nums[i-1] - nums[i]
#         if tmp % 2 == 0: # tmp为偶数
#             tmp = tmp // 2
#             for j in range(i):
#                 nums[j] -= tmp
#                 res[j] -= tmp
#             nums[i] += tmp+1
#             res[i] += tmp+1
#         else:
#             tmp = tmp // 2 +1
#             for j in range(i):
#                 nums[j] -= tmp
#                 res[j] -= tmp
#             nums[i] += tmp
#             res[i] += tmp
#     i+=1
# m1 = max(res)
# m2 = abs(min(res))
# m = m1+m2
# if m & 1 == 1:
#     print(m//2+1)
# else:
#     print(m//2)

n = int(input())
nums = list(map(int, input().split()))
res = (max(nums)-min(nums)) // 2
while True:
    tmp = nums[0] - res if nums[0]-res > 0 else 0
    find = True
    for i in range(1, len(nums)):
        index = False
        if nums[i] > tmp:
            if nums[i] - tmp > res:
                tmp = nums[i] - res
            else:
                tmp = tmp+1
            index = True
        elif nums[i] == tmp:
            tmp = tmp+1
            index = True
        else:
            if tmp - res >= nums[i]:
                break
            else:
                tmp = tmp+1
                index = True
        if not index:
            find = False
            break
    if find:
        break
    res+=1
print(res)