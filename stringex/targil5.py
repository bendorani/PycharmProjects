word=input("enter word: ")
letter=input("enter letter: ")
count=0
for i in word:
    if i==letter:
        count+=1
print(count)