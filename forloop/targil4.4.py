from random import randint
num=randint(0,100)
count=1
max=100
min=0
print(num)
guess=input("your number is (enter higher,lower or equal): ")
while guess!="equal":
    if guess=="higher":
        max=num
        num=randint(min+1,max)

    elif guess=="lower":
        min=num
        num=randint(min+1,max)

    count+=1
    print(num)
    guess = input("your number is (enter higher,lower or equal): ")
print(f"i took {count} guesses")