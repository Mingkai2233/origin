def func(grade):
    if len(grade) == 0:
        return 0
    avg = sum(grade.values()) / len(grade)
    print("平均分为:", avg)
    count = 0
    print("不及格的有:")
    for key, value in grade.items():
        if value < avg:
            count += 1
            print(key)
    print('不及格的人数为:', count)


grade = {'黎明': 90, '周伦': 85, '张丰': 55, '陈茹': 60, '李库': 58, '王小': 95}
func(grade)