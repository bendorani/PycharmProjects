from random import randint
list1=[randint(1,100) for i in range(10)]
tup=tuple(list1)
print(tup)
num=int(input("enter number: "))
tup+=num,
print(tup)
tup2=tuple(list1[:4])+ tuple(list1[9:5:-1])
print(tup2)
tup=list(tup)
tup.remove(tup[0])
tup=tuple(tup)
print(tup)
