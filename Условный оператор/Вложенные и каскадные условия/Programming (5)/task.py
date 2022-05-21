num1 = int(input())
num2 = int(input())
str1 = input()
if str1 == '+':
    print(num1 + num2)
elif str1 == '-':
    print(num1 - num2) 
elif str1 == '*':
    print(num1 * num2)    
elif str1 == '/' and num2 == 0:
    print('На ноль делить нельзя!')
elif str1 == '/':
    print(num1 / num2) 
else:
    print('Неверная операция')


