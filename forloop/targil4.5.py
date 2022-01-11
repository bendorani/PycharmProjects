num=int(input("enter how much numbers you want is the sidra: "))
num2=0
num3=1
if num==0:
    print()
elif num==1:
    print(0)
else:
    print(num2,num3,end=" ")
    for i in range(num-2):
        print(num2,end=" ")
        num4=num2+num3
        num2=num3
        num3=num4




