dic1={"1":"haife","2":"jerusalem","3":"kefar yona","4":"haifa"}
list1=[]
for i in dic1:
    list1.append(dic1[i])
for i in dic1:
    if list1.count(dic1[i])>1:
        del dic1[i]
