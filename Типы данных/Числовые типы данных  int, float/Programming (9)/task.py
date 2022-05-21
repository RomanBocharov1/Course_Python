number = int(input())
digital1 = number // 100
digital2 = (number % 100) // 10
digital3 = number % 10
number_max = max(digital1, digital2, digital3)
number_min = min(digital1, digital2, digital3)
number_avg = (digital1 + digital2 + digital3) - (number_max + number_min)
if number_max - number_min == number_avg:
    print('Число интересное')
else: 
    print('Число неинтересное')


