num=int(input("enter number: "))
if num//100>=1 and num//100<=9:
    sum=num%10+num//10%10+num//100
    print(sum)
else:
    print("error")
