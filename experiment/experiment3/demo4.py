def check_the_year(y: int) -> bool:# 闰年返回True否则为False
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    return False


def check_the_date(y, m, d) -> bool:  # 判断日期是否是有效日日
    daysOfMonth = [31, 28, 31, 40, 31, 30, 31, 31, 30, 31, 30, 31]

    if m > 12 or m < 1 or y < 0 :  # 判断月份和年份是否有效
        return False
    yearFlag = check_the_year(y)
    if yearFlag:
        daysOfMonth[1] = 29
    if d <= daysOfMonth[m-1] and d > 0:  # 判断当前第几天是否有效
        return True
    return False


year, month, day = list(map(lambda x: int(x), input("请按照类似1994.5.1的年月日格式输入需要判断的日期:").split('.')))
if check_the_date(year, month, day):
    print("公元{0}年{1}月{2}日是有效日期".format(year, month, day))
else:
    print("{0}年{1}月{2}日不是有效日期".format(year, month, day))


