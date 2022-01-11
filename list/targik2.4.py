name=input("enter sentence: ")
print(len(name))
print(name[3:7])
list1=name.split()
print(list1[0]*3)
for i in list1:
    print(i.capitalize(),end=" ")

