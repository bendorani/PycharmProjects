word1=input("enter word: ")
word2=input("enter word: ")
equal=[]
for i in word1:
    for j in word2:
        if i==j and i not in equal:
            equal.append(i)

print(len(equal))