number = int(input())
if number == 0:
    print('зеленый')
elif number >= 1 and number <= 10 and not(number % 2 == 0):
    print('красный')
elif number >= 1 and number <= 10 and number % 2 == 0:
    print('черный')  
elif number >= 11 and number <= 18 and not(number % 2 == 0):
    print('черный')
elif number >= 11 and number <= 18 and number % 2 == 0:
    print('красный')  
elif number >= 19 and number <= 28 and not(number % 2 == 0):
    print('красный')
elif number >= 19 and number <= 28 and number % 2 == 0:
    print('черный')
elif number >= 29 and number <= 36 and not(number % 2 == 0):
    print('черный')
elif number >= 29 and number <= 36 and number % 2 == 0:
    print('красный')
else:
    print('ошибка ввода')



