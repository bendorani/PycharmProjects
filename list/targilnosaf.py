from random import randint
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1[7:]
print(list2)
print(list1[::-1])
print(list1[1::2])
list3=list1[:5]
print(list3)
num=int(input("enter number: "))
list4=[1,2,3,4,5,6,7,num]
print(list4)
num2=int(input("enter number:"))
list5=[1,2,3,4,5,6,7,8,9,10]
list5[-3]=num2
del list5[9:7:-1]
print(list5)
list6=[]
for i in list1:
    if i%3==0:
        list6.append(i)
for i in list6:
    list1.remove(i)
print(list1,end=" ")
print(list6,end=" ")
print()
list7=[1,1]
for i in range(5):
    list7.append(sum(list7))
print(list7)

numberofuser=int(input("enter your number: "))
count=0
list8=[]
for i in range(20):
    randnum = randint(20, 100)
    if randnum!=numberofuser:
        list8.append(randnum)
    else:
        count+=1
print(list8)
print(count)
