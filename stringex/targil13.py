sentence=input("enter sentence: ")
letter=input("enter letter: ")
newsentence=""
for i in sentence:

    if i==letter:
        newsentence+=i.upper()
    else:
        newsentence += i
print(newsentence)