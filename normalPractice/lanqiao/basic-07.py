for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            tmp = i*100+j*10+k
            if tmp == i**3+j**3+k**3:
                print(tmp)