def find_in_list(list1:list,num,a):
    for i in range(list1[a],len(list1)):
        if num==list1[i]:
            return i
list1=[1,2,3,4,5,6,4,5]
print(find_in_list(list1,4,2))