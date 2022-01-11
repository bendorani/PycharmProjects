name=input("enter name: ")
newname=""
for i in name:
    if i!="a" and i!="A":
        newname+=i
print(newname)