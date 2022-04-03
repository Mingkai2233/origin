n = int(input())
nums = []
for i in range(n):
    num = input()
    nums.append(int(num, 16))
for i in range(n):
    print(oct(nums[i])[2:])
