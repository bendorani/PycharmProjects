def value_indic(dict1:dict):
    list1=[]
    for i in dict1:
        list1.append(dict1[i])
    return list1
dic1={1:"haifa",2:"jerusalem",3:"tel aviv"}
print(value_indic(dic1))