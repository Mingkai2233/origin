def dfsUnRecur(g: list):
    stack = [0]
    visted = {0}
    print(0, end=" ")
    while len(stack) > 0:
        cur = stack.pop()
        for j in range(len(g[cur])):
            if g[cur][j] != 0 and j not in visted:
                stack.append(cur)
                stack.append(j)
                visted.add(j)
                print(j, end=" ")
                break


if __name__ == "__main__":
    n = 7
    graph = [[0 for i in range(n)] for i in range(n)]
    data = [[0, 1], [0, 2], [1, 3], [1, 4], [4, 2], [2, 5], [2, 6], [6, 5]]
    for d in data:
        i, j = d
        graph[i][j] = 1

