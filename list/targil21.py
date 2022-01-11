from random import randint
str1=""
for i in range(4):
    j=str(randint(0,9))
    if j not in str1:
        str1+=j
bools=0
hits=0
num = input("enter 4 digits number guess: ")
while num!=str1:
    for i in num:
        if i in str1:
            bools+=1
    for j in range(len(num)):
        if num[j]==str1[j]:
            hits+=1
            bools-=1
    print(f"you got {bools} bools and {hits} hits")
    num = input("enter 4 digits number guess: ")
    bools=0
    hits=0
print("you got it")