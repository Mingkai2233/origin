from hashlib import md5
fileName = input("请输入要计算MD5值的文件名:")
try:
    file = open(fileName, 'rb')
except FileNotFoundError:
    print('文件不存在')
    exit()
except FileExistsError:
    print("文件存在异常")
    exit()
context = file.read()
md5Value = md5(context)
print("md5:", md5Value.hexdigest())