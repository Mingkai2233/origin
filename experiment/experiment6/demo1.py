import random

num = random.randint(0, 100)
print(num)
for i in range(5):
    n = int(input("请猜一个数(你还有{0}次机会):".format(4-i)))
    if n == num:
        print("恭喜你猜对了")
        break
    elif n < num:
        print("数太小了")
    else:
        print("数太大了")
