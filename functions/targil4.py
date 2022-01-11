def all_number(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum

for i in range(5):
    num = int(input("enter number: "))
    print(all_number(num))