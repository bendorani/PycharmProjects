def to_list(lis1):
    if type(lis1) in [dict,set,tuple,str]:
        list1=[i for i in lis1]
        return lis1

    else:
        print("invalid")
        return None

dic={1:"haifa",2:"jerusalem"}
tup=(1,2,3,4,5)

print(to_list(dic))
print(to_list(tup))
print(to_list(5))