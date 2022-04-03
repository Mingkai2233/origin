from treeNode import Node


# 常规写法
def lca1(head: Node, node1: Node, node2: Node):
    fatherMap = dict()
    fatherMap[head] = head
    process(head, fatherMap)
    fatherSet = set()
    while fatherMap[node1] is not node1:  # 根节点没有被放入fatherSet
        fatherSet.add(node1)
        node1 = fatherMap[node1]
    while fatherMap[node2] is not node2 and node2 not in fatherSet:  # 此步骤中如果fatherSet中没有node2的某个父节点,将会返回根节点,补充了上一步骤
        node2 = fatherMap[node2]

    return node2


def process(head: Node, fm: dict):
    if head is None:
        return
    if head.leftC is not None:
        fm[head.leftC] = head
    if head.rightC is not None:
        fm[head.rightC] = head
    process(head.leftC, fm)
    process(head.rightC, fm)


# 究极优化版本
def lca2(head: Node, node1, node2):
    if head is None or head is node1 or head is node2:  # base case
        return head
    left = lca2(head.leftC, node1, node2)
    right = lca2(head.rightC, node1, node2)
    if left is not None and right is not None:
        return head
    return left if left is not None else right


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
    find = lca2(root, nodes[8], nodes[7])
    print(find.value)