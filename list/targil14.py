num=int(input("enter number: "))
list1=[]
for i in range(1,num):
    if num%i==0:
        list1.append(i)
print(list1)