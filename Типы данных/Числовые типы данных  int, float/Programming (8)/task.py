number1 = int(input())
number2 = int(input())
number3 = int(input())
number_max = max(number1, number2, number3)
number_min = min(number1, number2, number3)
number_avg = (number1 + number2 + number3) - (number_max + number_min)
print(number_max)
print(number_avg)
print(number_min)


