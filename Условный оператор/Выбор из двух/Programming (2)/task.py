num = int(input())
num1 = num // 1000
num2 = (num // 100) % 10
num3 = (num % 100) // 10
num4 = num % 10
if num1 + num4 == num2 - num3:
    print('ДА')
else:
    print('НЕТ')





