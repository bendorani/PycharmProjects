sentence=input("enter sentence: ").split()
word=input("enter word: ")
word_index=[]
index_counter=0
for i in sentence:
    if i==word:
        index=sentence.index(i,index_counter)
        word_index.append(index)
        index_counter+=1
    else:
        index_counter+=1
print(word_index)