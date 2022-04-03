input_string = input()
chars = list(input_string)
while True:
    length = len(chars)
    flag = True
    if length < 3:
        flag = True
    else:
        for i in range(1, length-1):
            if ord(chars[i-1]) <= ord(chars[i]) <= ord(chars[i+1]):
                flag = False
                chars[i-1] = ''
                chars[i] = ''
                chars[i+1] = ''
                break
    chars = [i for i in chars if i != '']
    if flag:
        print("".join(chars))
        break

