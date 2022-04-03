from treeNode import Node
import math
import queue
#一般方法
# 判断二叉树是否为二叉搜索树(binary search tree)的一般方法, 如果一个为二叉搜索树,那么它中序遍历得到的一定是递增序列
preValue = -1  # 记录前一个节点d的值


def isBstRecur(head: Node):  # 用中序遍历的视角来看
    global preValue
    if head is None:
        return True
    if not isBstRecur(head.leftC):  # 判断左树是否为二叉搜索树
        return False

    if head.value <= preValue:  # 判断当前节点的值是否满足大于中序遍历的前一个结点
        return False
    else:
        preValue = head.value

    if not isBstRecur(head.rightC):  # 判断右树是否为二叉搜索树
        return False
    return True


def isBstUnRecur(head: Node):
    if head is None:
        return True
    global preValue
    stack = []
    while not len(stack) > 0 and head is not None:
        if head is not None:
            stack.append(head)
            head = head.leftC
        else:
            head = stack.pop()
            # 对节点进行操作
            if head.value > preValue:
                preValue = head.value
            else:
                return False
            head = head.rightC
    return True


# 判断一个二叉树是否为完全二叉树,基于宽度优先遍历
    # 1. 任意节点有右无左, 返回False
    # 2. 任意节点如果有左无右,那么接下来的节点需要全部为叶节点,否则返回False
def isCbt(head: Node):
    if head is None:
        return True
    q = queue.Queue(10)
    q.put(head)
    leaf = False
    while not q.empty():
        head = q.get()
        if head.rightC is not None and head.leftC is None:
            return False
        if head.leftC is not None and head.rightC is None:
            leaf = True

        if leaf is True:
            if head.leftC is not None or head.rightC is not None:
                return False
        else:
            if head.leftC is not None:
                q.put(head.leftC)
            if head.rightC is not None:
                q.put(head.rightC)
    return True


# 判断二叉树是否为满二叉树
# 套路方法,树形DP, 通过向左右子树请求数据来获得当前树返回的数据
    # 1. 罗列可能性
    # 2. 组织代码
# 判断二叉树是否为平衡二叉树(对于任何子树,左右子树高度相差不超过一)
class ReturnType1:
    balance = False
    height = 0

    def __init__(self, b, h):
        self.balance = b
        self.height = h


def isBalance(head: Node):
    if head is None:
        return ReturnType1(True, 0)
    leftData = isBalance(head.leftC)
    rightData = isBalance(head.rightC)
    balance = leftData.balance and rightData.balance and \
              math.fabs(leftData.height-rightData.height) < 2  # 左右树均为平衡树,并且左右树高度差不大于1
    height = max(leftData.height, rightData.height) + 1
    return ReturnType1(balance, height)


# 判断二叉树是否为二叉搜索树
class ReturnType2:
    def __init__(self, maxvalue, minvalue, isb):
        self.maxValue = maxvalue
        self.minValue = minvalue
        self.isB = isb


def isBst(head: Node) -> ReturnType2:
    if head is None:
        return None
    leftData = isBst(head.leftC)
    rightData = isBst(head.rightC)
    maxValue = head.value
    minValue = head.value
    # 计算当前树的最大值和最小值
    if leftData is not None:
        maxValue = max(leftData.maxValue, maxValue)
        minValue = min(leftData.minValue, minValue)
    if rightData is not None:
        maxValue = max(rightData.maxValue, maxValue)
        minValue = min(rightData.minValue, minValue)
    isbst = True
    # 判断当前树是否为二叉搜索树
    if leftData is not None and (not leftData.isB or leftData.maxValue >= head.value):
        isbst = False
    if rightData is not None and (not rightData.isB or rightData.minValue <= head.value):
        isbst = False
    return ReturnType2(maxValue, minValue, isbst)


# 判断是否为满二叉树
class ReturnType3:
    def __init__(self, d, n):
        self.depth = d
        self.nodes = n


def process(head: Node) -> ReturnType3:
    if head is None:
        return ReturnType3(0, 0)
    leftData = process(head.leftC)
    rightData = process(head.rightC)
    d = max(leftData.depth, rightData.depth) + 1
    n = leftData.nodes + rightData.nodes + 1
    return ReturnType3(d, n)


def isFull(head: Node):
    data = process(head)
    depth = data.depth
    n = data.nodes
    return n == int(2**depth-1)


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
    print(isCbt(root))


