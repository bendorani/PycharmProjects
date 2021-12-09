num=int(input("enter number: "))
while num>=100 and num<=999:
    print(f"{num//10%10+num%10+num//100}")
    num=int(input("enter number: "))
print("error")