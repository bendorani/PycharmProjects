str1=input("enter string: ")
str2=input("enter string: ")
str3=input("enter string: ")
str4=input("enter string: ")
str5=input("enter string: ")
list1=[str1,str2,str3,str4,str5]
count=0
for i in list1:
    if len(i)>=4 and i[0]==i[len(i)-1]:
        count+=1
print(count)