class UnionFindSet:
    def __init__(self, elements: list):
        self.elements = set()  # 存储并查集中的所有元素,用于判断元素是否在并查集中
        self.fatherMap = dict()  # key为元素,value为其所在集合的代表元素
        self.sizeMap = dict()  # key为代表元素, value为其所代表集合的大小
        for i in elements:
            self.elements.add(i)
            self.fatherMap[i] = i
            self.sizeMap[i] = 1

    def findHead(self, element):  # 寻找过程中顺带将结构扁平化,将本集合中所有元素直接指向代表元素,提高效率
        tmp = []  # 存储找父亲过程中经过的元素
        while self.fatherMap[element] != element:
            tmp.append(element)
            element = self.fatherMap[element]
        for e in tmp:
            self.fatherMap[e] = element  # 上一步循环推出后element即为代表元素
        return element

    def isSameSet(self, element1, element2):
        if element1 in self.elements and element2 in self.elements:
            return self.findHead(element1) is self.findHead(element2)
        return False

    def union(self, element1, element2):
        if element1 in self.elements and element2 in self.elements:
            if not self.isSameSet(element1, element2):
                head1 = self.findHead(element1)
                head2 = self.findHead(element2)
                if self.sizeMap[head1] > self.sizeMap[head2]:
                    self.sizeMap[head1] += self.sizeMap[head2]
                    del self.sizeMap[head2]
                    self.fatherMap[head2] = head1
                else:
                    self.sizeMap[head2] += self.sizeMap[head1]
                    del self.sizeMap[head1]
                    self.fatherMap[head1] = head2


ufs = UnionFindSet([1,2,3,4,5,6])
ufs.union(1,2)
print(ufs.fatherMap[1], ufs.sizeMap[ufs.findHead(1)])