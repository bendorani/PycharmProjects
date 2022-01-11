def all_number(a,b):
    for i in range(a,b+1):
        print(i,end=" ")
def bigeer(a,b):
    if a>b:
        return a
    else:
        return b
def lower(a,b):
    if a<b:
        return a
    else:
        return b

num1=int(input("enter number: "))
num2=int(input("enter number: "))
all_number(lower(num1,num2),bigeer(num1,num2))