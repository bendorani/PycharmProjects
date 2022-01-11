def category_age(num):
    if 0<=age<=18:
        return "child"
    elif 19<=age<=60:
        return "adult"
    elif 61<=age<=120:
        return "senior"

for i in range(5):
    age=int(input("enter age: "))
    print(category_age(age))