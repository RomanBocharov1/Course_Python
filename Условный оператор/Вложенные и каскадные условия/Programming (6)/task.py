color1 = input()
color2 = input()
red = 'красный'
blue = 'синий'
yellow = 'желтый'
if color1 == red and color2 == blue:
    print('фиолетовый')
elif color1 == red and color2 == yellow:
    print('оранжевый')
elif color1 == blue and color2 == yellow:
    print('зеленый')
elif color1 == blue and color2 == red:
    print('фиолетовый')
elif color1 == yellow and color2 == red:
    print('оранжевый')
elif color1 == yellow and color2 == blue:
    print('зеленый')
elif color1 == red and color2 == red:
    print('красный')
elif color1 == yellow and color2 == yellow:
    print('желтый')
elif color1 == blue and color2 == blue:
    print('синий')
else:
    print('ошибка цвета')



