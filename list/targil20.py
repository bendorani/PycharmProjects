from random import randint
num=int(input("enter number: "))
list1=[randint(1,10) for i in range(10)]
print(list1)
for i in range(len(list1)):
    if list1[i]==num:
        print(i)
        break
else:
    input("num not in list")