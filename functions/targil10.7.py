def no_duplicates(list1:list):
    list1=list(set(list1))
    return list1
list1=[1,2,3,3,3,3,4,5]
print(no_duplicates(list1))
