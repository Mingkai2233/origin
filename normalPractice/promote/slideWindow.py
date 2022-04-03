import collections


class SlideWindow:
    def __init__(self, nums: list, initsize: int):
        self.nums = nums[:]
        self.size = initsize  # window size
        self.ledge = -1
        self.redge = -1
        self.dq = collections.deque()
        for i in range(initsize):
            self.moveright()

    def moveright(self):  # 窗口右边界右移一位
        if not(self.redge < len(self.nums)-1):
            return False
        self.redge += 1
        while len(self.dq) > 0:
            tmp = self.dq.pop()
            if self.nums[tmp] >= self.nums[self.redge]:
                self.dq.append(tmp)
                self.dq.append(self.redge)
                break
        if len(self.dq) == 0:
            self.dq.append(self.redge)

    def moveleft(self):  # 窗口左边界右移一位
        if not(self.ledge < self.redge):
            return False
        self.ledge += 1
        while len(self.dq) > 0:  # 从双端队列头开始判断,将窗口外的元素移除
            tmp = self.dq.popleft()
            if tmp > self.ledge:
                self.dq.appendleft(tmp)
                break

    def getMax(self):  # 获得当前窗口中的最大值
        tmp = self.dq.popleft()
        self.dq.appendleft(tmp)
        return self.nums[tmp]


list1 = [6,4,3,5]
sw = SlideWindow(list1, 2)
sw.moveright()
print(sw.getMax())
sw.moveright()
print(sw.getMax())
sw.moveleft()
print(sw.getMax())
