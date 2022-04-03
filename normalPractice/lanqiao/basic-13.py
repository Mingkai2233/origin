n = int(input())
if n >= 1 and n <= 200:
    nums = list(map(int, input().split()))
    nums.sort()
    for i in range(len(nums)):
        print(nums[i], end=" ")