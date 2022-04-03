import random
n = 10000
one = 0
two = 0
three = 0
four = 0

for i in range(n):
    result = random.randint(0, 360)
    if result < 20:
        one += 1
    elif result < 100:
        two += 1
    elif result < 220:
        three += 1
    else:
        four += 1
print("一等奖次数:", one)
print("二等奖次数:", two)
print("三等奖次数:", three)
print("四等奖次数:", four)