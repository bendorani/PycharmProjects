def grades_of_students(a):
    list1=[]
    for i in range(a):
        grade=input("enter grade: ")
        list1.append(grade)
    return list1
def average_grade(list=[]):
    sum=0
    for i in list:
        sum+=int(i)
    return sum//len(list)

num=int(input("enter number of students: "))
print(average_grade(grades_of_students(num)))



