num=int(input("enter  number: "))
while num>=10 and num<=99:
    if num%7==0 or num%10==7 or num//10==7:
        print("this is a lucky number")
    else:
        print("this is not a lucky number")
    num = int(input("enter  number: "))
print("you didnt enter a two digit number")