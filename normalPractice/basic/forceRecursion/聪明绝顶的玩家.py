# 给定一个列表,玩家A和B依次从中选择一个数字作为自己的分数,只能从左右两侧选一个,并且A先手,输出最后赢家的分数
def firstChoose(nums: list, left, right):
    if left == right:  # 如果最后只剩一个,由于是先手,所以直接将最后一个拿走
        return nums[left]
    return max(nums[left]+secondChoose(nums, left+1, right),
               nums[right]+secondChoose(nums, left, right-1))  # 先手选择最大的


def secondChoose(nums: list, left, right):
    if left == right:  # 后手,剩最后一个的时候,已经被先手的拿走了
        return 0
    return min(firstChoose(nums, left+1, right),
               firstChoose(nums, left, right-1))  # 后手的时候只能选择小的,因为大的已经被先手选走.


def win(nums):
    if nums is None or len(nums) < 1:
        return 0
    return max(firstChoose(nums, 0, len(nums)-1),
               secondChoose(nums, 0, len(nums)-1))


scores = [1, 2, 10, 40]
print(win(scores))