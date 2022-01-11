def tupels_dict(dict1:dict):
    list1=[]
    tup1=()
    for i in dict1:
        tup1=(i,dict1[i],)
        list1.append(tup1)
    return list1
dic={1:"haifa",2:"jerusalem",3:"tel aviv"}
print(tupels_dict(dic))
