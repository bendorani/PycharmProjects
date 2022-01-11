list1=[1,3,2,3,4,5,6,4,3,2,2,1]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)