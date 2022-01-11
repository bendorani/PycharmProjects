list1=[1,2,3,4,7,7,8,3,"a"]
list2=[5,6,9,"a",0,6,5,"b","b","c","d"]
print(list1)
print(list2)
for i in list1:
    if i in list2:
        print(f"{i} in both lists ")