num1 = int(input())
num2 = int(input())
num3 = int(input())
if num2 > num1 and num1 > num3:
    print(num1)
elif num1 < num1 and num1 < num3:
    print(num2)  
elif num1 < num2 and num2 < num3:
    print(num2)
elif num1 > num2 and num2 > num3:
    print(num2)    
else:
    print(num3)



