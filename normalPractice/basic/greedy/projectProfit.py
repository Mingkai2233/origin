import queue


class Project:
    def __init__(self, cost, profit):
        self.cost = cost
        self.profit = profit

    def __lt__(self, other):
        return self.profit < other.profit


def getTheMostMoney(costs: list, profits, money, amount):
    projects = [Project(costs[i], profits[i]) for i in range(len(costs))]
    bigProfitH = queue.PriorityQueue()
    projects.sort(key=lambda x: x.cost, reverse=True)
    n = 0
    while n < amount:
        while len(projects) > 0:  # 将当前资金能够支持的项目加入到一个大根堆中
            index = len(projects)-1
            if money > projects[index].cost:
                project = projects.pop()
                bigProfitH.put(-project.profit)
            else:
                break
        if bigProfitH.empty():  # 表明当前资金不足以支持任何项目,无法完成指定个数的项目
            break
        else:
            money += -bigProfitH.get()
            n += 1
    return money


if __name__ == "__main__":
    c = [1, 3, 2, 1, 6, 9]  # 项目的成本
    p = [1, 2, 1, 2, 3, 4]  # 项目的利润
    m = 2  # 起始资金
    a = 5  # 最大项目数
    result = getTheMostMoney(c, p, m, a)
    print(result)