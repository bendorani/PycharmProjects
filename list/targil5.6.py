list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1[7:]
print(list2[::-1])
print(list1[::2])
list3=list1[::2]
print(list3)
num1=int(input("enter number: "))
num2=int(input("enter number: "))
num3=int(input("enter number: "))

list4=[1,2,3,4,5,6,7,8,9,10]

print(list4)
for i in range(len(list1)):
    list1[i]*=2
print(list1)
list5=[list1[0]//2,list1[9]//2]
print(list5)

