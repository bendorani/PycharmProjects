name=input("enter number: ")
dic1={"1":"israel","2":"france","3":"china"}
for i in dic1:
    if i==name:
        print(f"{name} exict")
        break
else:
    print(f"{name} not exist")