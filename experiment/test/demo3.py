key = input("请输入密码:")
length = len(key)
if length < 6:
    print("这个字符串不能作为密码")
    exit()
num = 0
lowchar = 0
bigchar = 0
punc = 0
for c in key:
    c = ord(c)
    if ord('a') <= c <= ord('z'):
        lowchar += 1
    elif ord("A") <= c <= ord("z"):
        bigchar += 1
    elif ord("0") <= c <= ord("9"):
        num += 1
    else:
        punc += 1
if length >= 8:
    if num != 0 and lowchar != 0 and bigchar != 0 and punc != 0:
        print("强密码")
    elif not (num == 0 and lowchar == 0 and bigchar == 0 and punc == 0):
        print("弱密码")
else:
    if num != 0 and lowchar != 0 and bigchar != 0 and punc != 0:
        print("弱密码")
    else:
        print("不能作为密码")
