num=int(input("enter number: "))
num2=int(input("enter second number: "))
while num%2==0 and num2%2==0:
    print(num+num2)
    num = int(input("enter number: "))
    num2 = int(input("enter second number: "))
print(num*num2)