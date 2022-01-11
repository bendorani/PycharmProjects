def sum_even(list1:list):
    sum=0
    for i in list1:
        if i%2==0:
            sum+=i
    return sum
list1=[1,2,3,4,5,6,7,8]
print(sum_even(list1))
