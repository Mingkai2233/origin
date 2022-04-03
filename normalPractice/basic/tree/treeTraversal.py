import queue
from treeNode import Node


#  递归方式
def preOrderRecur(head: Node):
    if head is None:
        return
    print(head.value)
    preOrderRecur(head.leftC)
    preOrderRecur(head.rightC)


def inOrderRecur(head: Node):
    if head is None:
        return
    inOrderRecur(head.leftC)
    print(head.value)
    inOrderRecur(head.rightC)


def posOrderRecur(head: Node):
    if head is None:
        return
    posOrderRecur(head.leftC)
    posOrderRecur(head.rightC)
    print(head.value)


# 非递归
def preOrderUnRecur(head: Node):
    #  流程:1. 栈中弹出一个节点
    #      2. 将该节点输出
    #      3. 将节点的非空左右孩子入栈, 先右后左
    #      4. 跳回1
    stack = [head]
    if head is not None:
        while len(stack) > 0:
            head = stack.pop()
            print(head.value)
            if head.rightC is not None:
                stack.append(head.rightC)
            if head.leftC is not None:
                stack.append(head.leftC)


def posOrderUnRecur(head: Node):
    #  流程:1. 栈中弹出一个节点
    #      2. 将该节点入收集栈
    #      3. 将节点的非空左右孩子入栈, 先左后右
    #      4. 跳回1
    if head is not None:
        stack1 = [head]
        stack2 = []
        while len(stack1) > 0:
            head = stack1.pop()
            stack2.append(head.value)
            if head.leftC is not None:
                stack1.append(head.leftC)
            if head.rightC is not None:
                stack1.append(head.rightC)
    while len(stack2) > 0:
        print(stack2.pop())


def inOrderUnRecur(head: Node):
    if head is not None:
        stack = []
        #  将树的左边界全部入栈,然后弹出一个节点,对相应的右孩子节点对应的子树进行同样操作
        while len(stack) > 0 or head is not None:
            if head is not None:
                stack.append(head)
                head = head.leftC
            else:
                head = stack.pop()
                print(head.value)
                head = head.rightC


#  树的宽度优先遍历
def breadthFirstTraversal(head: Node):
    if head is None:
        return
    q = queue.Queue(10)
    q.put(head)
    while not q.empty():
        head = q.get()
        print(head.value)
        if head.leftC is not None:
            q.put(head.leftC)
        if head.rightC is not None:
            q.put(head.rightC)


#  获得树的最大宽度,宽度优先遍历应用
def getTheMaxBreadth1(head: Node):
    if head is None:
        return
    q = queue.Queue(10)
    levelMap = dict()  # 记录每个节点所在的层
    curLevel = 0  # 当前所在层数
    curLevelNodes = 0  # 当前所在层的节点数量
    maxNodes = 0  # 最大节点数
    levelMap[head] = curLevel
    q.put(head)

    while not q.empty():
        head = q.get()
        if levelMap[head] == curLevel:
            curLevelNodes += 1
        else:
            curLevel += 1
            maxNodes = curLevelNodes if curLevelNodes > maxNodes else maxNodes
            curLevelNodes = 1
        if head.leftC is not None:
            q.put(head.leftC)
            levelMap[head.leftC] = curLevel + 1
        if head.rightC is not None:
            q.put(head.rightC)
            levelMap[head.rightC] = curLevel + 1
    return maxNodes


#  优化版获得最大宽度
def getTheMaxBreadth2(head: Node):
    if head is None:
        return
    q = queue.Queue(10)
    q.put(head)
    curEnd = head  # 记录当前行的结尾节点
    nextEnd = None  # 记录下一行的结尾节点,当前队列尾部的节点为下一层的结尾节点
    curLevelNodes = 0
    maxNodes = 0
    while not q.empty():
        head = q.get()
        curLevelNodes += 1
        if head.leftC is not None:
            q.put(head.leftC)
            nextEnd = head.leftC
        if head.rightC is not None:
            q.put(head.rightC)
            nextEnd = head.rightC
        if head == curEnd:
            curEnd = nextEnd
            nextEnd = None
            if curLevelNodes > maxNodes:
                maxNodes = curLevelNodes
            curLevelNodes = 0
    return maxNodes


if __name__ == '__main__':
    nodes = [None]
    for i in range(1, 8):
        nodes.append(Node(i))
    nodes[1].leftC = nodes[2]
    nodes[1].rightC = nodes[3]
    nodes[2].leftC = nodes[4]
    nodes[2].rightC = nodes[5]
    nodes[3].rightC = nodes[6]
    nodes[6].leftC = nodes[7]
    root = nodes[1]
    print(getTheMaxBreadth1(root))
    print(getTheMaxBreadth2(root))

    nodes = [0]
    for i in range(1, 9):
        nodes.append(Node(i))
    nodes[1].leftC = nodes[2]
    nodes[1].rightC = nodes[3]
    nodes[2].rightC = nodes[4]
    nodes[3].leftC = nodes[5]
    nodes[3].rightC = nodes[6]
    nodes[5].leftC = nodes[7]
    nodes[6].rightC = nodes[8]
    root = nodes[1]
    print(getTheMaxBreadth2(root))