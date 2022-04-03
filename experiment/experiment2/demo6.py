# test_strings = ['byzantium', 'byzantine', 'byzants', 'byzantinism']
# 输入
test_strings = []
n = int(input())
for i in range(n):
    print('第{0}个单词:'.format(i+1))
    test_strings.append(input())
max_len = 0
wordLenmin = 100
# 找到最短的单词的长度
for i in test_strings:
    tmp = len(i)
    if tmp < wordLenmin:
        wordLenmin = tmp
flag = False
# 找最大前缀
for i in range(wordLenmin):
    tmp = test_strings[0][:max_len+1]
    for word in test_strings:
        if word[:max_len+1] != tmp:
            flag = True
            break
    if flag:
        break
    max_len += 1

if max_len == 0:
    print("无最大公共前缀")
else:
    print("最大公共前缀为:", test_strings[0][:max_len])

