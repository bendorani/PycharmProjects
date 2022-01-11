from random import randint
list1=[randint(0,10) for i in range(10)]
print(list1)
list2=[]
for i in list1:
    if i not in list2:
       list2.append(i)
for i in list2:
    print(f"{i} is {list1.count(i)} times in list")

