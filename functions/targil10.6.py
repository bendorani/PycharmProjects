def upper_and_lower(str1:str):
    countlower=0
    countupper=0
    for i in str1:
        if i.islower():
            countlower+=1
        elif i.isupper():
            countupper+=1
    print(f"number of lower letter:{countlower}")
    print(f"number of upper letters:{countupper}")
str1="ABcdeA1"
upper_and_lower(str1)