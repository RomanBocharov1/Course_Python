abc = int(input())

a = abc // 100
b = (abc // 10) % 10
c = abc % 10

print(a, b, c, sep = '')
print(a, c, b, sep = '')
print(b, a, c, sep = '')
print(b, c, a, sep = '')
print(c, a, b, sep = '')
print(c, b, a, sep = '')