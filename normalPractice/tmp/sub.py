def process(nums, i):
    if i == len(nums):
        print(nums)
        return
    process(nums, i+1)  # 要第i位
    tmp = nums[i]
    nums[i] = "#"
    process(nums, i+1)
    nums[i] = tmp


def sub(nums: list):
    process(nums, 0)


l = [1, 2, 3, 4]
sub(l)