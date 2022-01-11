def three_digit(num):
    if 100<=num<=999:
        return True
    else:
        return False
def sum_three_digits(num):
    sum=num%10+num//10%10+num//100
    return  sum

num=int(input("enter number: " ))
if three_digit(num):
    print("number is three digit")
    print(f"sum digits is:{sum_three_digits(num)}")
else:
    print("number is not three digits")
