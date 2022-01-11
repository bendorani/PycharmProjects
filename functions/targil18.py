def max_in_list(list1:list):
    max=0
    for i in list1:
        if i>max:
            max=i
    return max
list1=[1,2,3,4,5,6]
print(max_in_list(list1))