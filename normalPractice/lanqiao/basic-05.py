input()
nums = list(map(int, input().split()))
target = int(input())
if target in nums:
    print(nums.index(target)+1)
else:
    print(-1)