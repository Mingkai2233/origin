def countIsland(island: list) -> int:
    if island is None or island[0] is None:
        return 0
    row = len(island)
    col = len(island[0])
    res = 0
    for i in range(row):
        for j in range(col):
            if island[i][j] == 1:
                res += 1
                infect(island, i, j, row, col)
    return res


def infect(island, i, j, row, col):
    if i < 0 or i >= row or j < 0 or j >= col or island[i][j] != 1:
        return
    island[i][j] = 2
    print(island)
    infect(island, i+1, j, row, col)
    infect(island, i-1, j, row, col)
    infect(island, i, j+1, row, col)
    infect(island, i, j-1, row, col)


if __name__ == '__main__':
    matrix =[[0, 0, 1, 0, 1, 0],
             [1, 1, 1, 0, 1, 0],
             [1, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 1]]
    print(countIsland(matrix))