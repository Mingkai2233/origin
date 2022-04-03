n = int(input())
videos = list(map(str, list(range(1, n+1))))
videos.sort()
for i in range(50):
    print(videos[i])