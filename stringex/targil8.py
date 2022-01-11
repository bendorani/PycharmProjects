word=input("enter word:")
newword=""
for i in word:
    if word.count(i)>1 and i not in newword:
        newword+=i
print(f"{newword} are the letter that duplicate in the word")