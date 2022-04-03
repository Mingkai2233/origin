import re
test_string = 'a_123_b'
test_string = input("请输入字符串:")
pattern1 = '^[a-zA-Z_][0-9a-zA-Z_]*$'
pattern2 = '^\d+abc$'
pattern3 = '^-*\d+$'

result = re.search(pattern3, test_string) != None
if result:
    print("字符串合法")
else:
    print("字符串非法")
