from random import randint
def rand_list(list=[]):
    for i in range(20):
        list.append(randint(1,100))

def count_numlist(a,list1=[]):
    return list1.count(a)
def index_max(list=[]):
    return list.index(max(list))
list2=[]
rand_list(list2)
print(list2)
num=int(input("enter number: "))
print(f"number is {count_numlist(num,list2)} times in list")
print(f"the index of the bigest number in list is: {index_max(list2)}")
