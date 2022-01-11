def multipe_list(list1:list):
    sum=1
    for i in list1:
        sum*=i
    return sum
list1=[7,-1,3,2,8]
print(multipe_list(list1))