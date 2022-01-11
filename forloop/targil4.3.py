from random import randint
num=randint(1,9)
count=1
usernumber=int(input("enter guess: "))
while usernumber!=num:
    if(usernumber>num):
        print("your number is higher")
    else:
        print("your number is low")
    count+=1
    usernumber = int(input("enter guess: "))
print(f" you took {count} guesses")