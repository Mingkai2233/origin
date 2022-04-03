test_string = input("请输入一个以'.'分割的单词序列:")
test_string = '.'+test_string
str_len = len(test_string)
front = str_len - 1
behind = str_len
result = []

while front >= 0: # 扫描字符串,定位单词
    if test_string[front] == '.':
        result += test_string[front:behind]
        behind = front
    front -= 1

result = result[1:]
result = ''.join(result) # 对结果进行处理
print(result)
