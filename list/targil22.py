from random import randint,choice
listword=["football","ball","pillow","computer","game","baloon","banana","apple","car","risk","fridge","kitchen","note","bottle"]
name=choice(listword)
print(name)
list2=["_" for i in name]

i=0
letter = input("enter letter: ")
while i<7 :
    for j in range(len(name)):
        if letter==name[j]:
            list2[j]=letter
            print(tuple(list2))
    if "_" not in list2:
        print("you sucseed")
        break
    else:
        print("keep trying")
        i += 1
        letter = input("enter letter: ")
if i==7:
    print("you failed")



