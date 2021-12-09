num=int(input("enter number: "))
num2=int(input("enter number 2: "))
while num>num2:
    num2+=1
    if num2%2==0 and num2!=num:
        print(num2)
while num2>num:
    num+=1
    if num%2==0 and num!=num2:
        print(num)