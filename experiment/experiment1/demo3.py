nums = list(map(lambda x: int(x), input("请输入十个不大于十的自然数数:").split(" ")))
nums1 = list(map(lambda x: x**3, nums))
print(nums1)
print(nums[4:8])
print(nums[-5:])
nums2 = [i**2 for i in nums if i % 2 ==  0]
print(nums2)