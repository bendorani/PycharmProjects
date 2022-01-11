word=input("enter word: ")
letter=input("enter letter: ")
while letter in word:
    print(word.index(letter))
    break
else:
    print("letter isnt in word")