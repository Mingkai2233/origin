total = 0
def subsequence(i: int, chars: list):
    if i == len(chars):
        global total
        total += 1
        print(''.join(chars))
    else:
        subsequence(i+1, chars)
        tmp = chars[i]
        chars[i] = '*'
        subsequence(i+1, chars)
        chars[i] = tmp

string = 'abcd'
string = list(string)
subsequence(0, string)
