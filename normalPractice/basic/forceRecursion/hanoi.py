def hanoi(n: int):
    if n > 0:
        move(n, 'left', 'right', 'other')


def move(i, begin, end, other):
    if i == 1:
        print('move {0} from {1} to {2}'.format(i, begin, end))
    else:
        move(i-1, begin, other, end)
        print('move {0} from {1} to {2}'.format(i, begin, end))
        move(i-1, other, end, begin)


hanoi(3)