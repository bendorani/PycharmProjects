num=int(input("enter number: "))
sum=0
count=0
while 0<=num<=100:
    if(num>60):
        sum+=num
        count+=1
    
    num = int(input("enter number: "))
print(sum)
print(sum/count)