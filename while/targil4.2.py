# num=int(input("enter number: "))
# x=2
# while num%x!=0:
#     x+=1
#     if(num==x):
#         print(f"{num} is מספר ראשוני")
# if num==2:
#     print(f"{num} is מספר ראשוני")

num=int(input("enter number: "))
x=2

while x<num and x=="false":
    if num%x==0:
        print("number isnt ראשוני")
        x=bool("false")
    else:
        x+=1
print("nubmer is ראשוני")
