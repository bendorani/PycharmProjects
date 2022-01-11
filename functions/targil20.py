def remove_fromlist(list1:list,value):
    location=list1.index(value)
    list1[location:location+1]=[]
    return list1

list2=[1,2,3,4,5,6]
print(remove_fromlist(list2,4))
print(id(list2))

