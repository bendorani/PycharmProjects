def calculater(a,b):
    return a+b,a-b,a*b,a/b
num1=int(input("enter number: "))
num2=int(input("enter second number: "))
cal=calculater(num1,num2)
print(cal)
sum=cal[0]
print(sum)
