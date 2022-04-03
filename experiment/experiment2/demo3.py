# test_string = 'python'
# key = '12345'
test_string = input("请输入待加密/解密的字符串:")
key = input('请输入密钥:')
choice = int(input("加密请输入1, 解密请输入2:"))
# 对用户输入进行判断
if choice == 1:
    choice = True
elif choice == 2:
    choice = False
else:
    exit()

str_length = len(test_string)
key_length = len(key)
result = []
if choice:
    for i in range(str_length):
        result.append(chr((ord(test_string[i])+ord(key[i % key_length])) % 128))
else:
    for i in range(str_length):
        result.append(chr((ord(test_string[i])-ord(key[i % key_length])) % 128))
print(''.join(result))
