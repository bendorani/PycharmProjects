def average(*args):
    sum=0
    for i in args:
        sum+=i
    return sum/len(args)
def print_details(name,age,salary=0):
    for i in range(5):
        print(name,age,salary,end="//")
print_details("ben",15)
print()
print(average(1,2,3,4,5,6))