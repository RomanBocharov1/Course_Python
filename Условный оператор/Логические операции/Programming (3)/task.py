number = int(input())
if number >= 1000 and number <= 9999 and (number % 7 == 0 or number % 17 == 0):
    print('YES')
else:
    print('NO')



