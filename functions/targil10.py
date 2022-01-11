def is_pass(a):
    if 70<=a<=100:
        return True
    else:
        return False

for i in range(5):
    grade=int(input("enter grade: "))
    if is_pass(grade):
        print("pass")
    else:
        print("failed")