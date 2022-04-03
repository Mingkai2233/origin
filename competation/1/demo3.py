num = input()
k = int(input())
num_list = list(num)
length = len(num_list)
num_list.sort(reverse=True)
result = [num_list[i] for i in range(length-k)]
print("".join(result))

