list1=[]
list2=[]
number=int(input("enter number for first list: "))
while number!=-1:
    list1.append(number)
    number = int(input("enter number for first list: "))
number2=int(input("enter number for second list: "))
while number2!=-1:
    list2.append(number2)
    number2 = int(input("enter number for second list: "))
list3=list1+list2
print(list3)
print(len(list3))