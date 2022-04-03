import collections
test_string = input('请输入一个要统计的字符串:')
test_string = test_string.lower()
cnt = collections.Counter(test_string)
cnt = dict(cnt)
# 统计各种字符的数量
num = 0
character = 0
space = 0
other = 0
for key, value in cnt.items():
    tmp = ord(key)
    if tmp >= ord('0') and tmp <= ord('9'):  # 判断是否为数字
        num += value
    elif tmp >= ord('a') and tmp <= ord('z'):  # 判断是否为字母
        character += value
    elif tmp == ord(' '):  # 判断是否为空格
        space += value
    else:  # 判断是否为其他字符
        other += value
print("num:", num, '  character:', character, '  space:', space, '  other:', other)