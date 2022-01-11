list1=[]
grade=int(input("enter grade: "))
countpass=0
countfail=0
while grade!=-1:
    list1.append(grade)
    if grade>=60:
        countpass+=1
    else:
        countfail+=1
    grade=int(input("enter grade: "))
print(list1)
print(f"{countpass} passed")
print(f"{countfail} failed")