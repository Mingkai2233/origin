# 不借助其他数据结构将一个栈进行反转
def getTheBottom(stack: list):
    tmp = stack.pop()
    if not len(stack) > 0:
        return tmp
    else:
        last = getTheBottom(stack)
        stack.append(tmp)
        return last


def reverse(stack: list):
    if not len(stack) > 0:
        return
    tmp = getTheBottom(stack)  # 获得栈底元素,借助系统栈进行保存
    reverse(stack)  # 进入递归
    stack.append(tmp)  # 压入


list1 = [1, 2, 3]
reverse(list1)
print(list1)