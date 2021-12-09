num=int(input("enter number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
if num>num2 and num>num3:
    print(num)
elif num2>num and num2>num3:
    print(num2)
else:
    print(num3)