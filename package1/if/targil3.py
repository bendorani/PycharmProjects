age=int(input("enter age: "))
if age>=0 and age<=18:
    print("child")
elif age>=19 and age<=60:
    print("adult")
elif age>=61 and age<=120:
    print("senior")
else:
    print("you need to enter age between 0-120")