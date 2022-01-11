num=int(input("enter number: "))
for i in range(2,num):
    if(num%i==0):
        print(f"number is not first number: ")
        break
else:
    print(f"number is first")

