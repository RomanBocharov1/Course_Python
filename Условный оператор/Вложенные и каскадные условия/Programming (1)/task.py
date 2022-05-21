side1 = int(input())
side2 = int(input())
side3 = int(input())
if side1 == side2 and side2 == side3 and side1 == side3:
    print('Равносторонний')
elif side1 != side2 and side1 != side3 and side2 != side3:
    print('Разносторонний')
else:
    print('Равнобедренный')

