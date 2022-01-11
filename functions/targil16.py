def number_in_list(list1:list,num):
    count=0
    for i in list1:
        if i==num:
            count+=1
    return count
list1=[1,2,3,4,5,4,4]
print(number_in_list(list1,4))