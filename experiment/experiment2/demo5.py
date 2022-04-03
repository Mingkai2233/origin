import re
test_string = 'ac34he123ij89mlopd90kkk'
test_string = input("请输入字符串:")
result = re.findall('\d+', test_string)
total = 0
for i in result:
    total += int(i)
print(total)
