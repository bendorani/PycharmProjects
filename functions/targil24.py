def set_list(list1:list):
    set1=set()
    for i in list1:
        if i not in set1:
            set1.add(i)
    return set1
list1=[1,2,3,4,5,4,3,6]
print(set_list(list1))