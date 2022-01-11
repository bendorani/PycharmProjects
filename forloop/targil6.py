num = int(input("enter number: "))
sumpass= 0
countpass = 0
sumfail=0
countfail=0
while 0 <= num <= 100:
    if (num > 60):
        sumpass += num
        countpass += 1
    else:
        sumfail+=num
        countfail+=1

    num = int(input("enter number: "))
print(f"sum pass:{sumpass}")
print(f"averge pass:{sumpass / countpass}")
print(f"sum fail:{sumfail}")
print(f"averge fail:{sumfail/countfail}")