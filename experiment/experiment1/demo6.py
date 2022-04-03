nums = input("第一问:")
total = 0
for i in nums:
    total += int(i)
print(total)

setA = input('第二问第一个集合:')
setB = input('第二问第二个集合:')
setA = set(setA)
setB = set(setB)
print('交集:', setA & setB)
print('并集:', setA | setB)
print('差集:', setA - setB)


num = int(input('第三问:'))
print('二进制:',bin(num) )
print('八进制:', oct(num))
print('十六进制:', hex(num) )