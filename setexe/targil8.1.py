set1={1,2,3,4,5,6}
set2={4,5,7,8,1,9}
set3=set()
for i in set1:
    set3.add(i)
for j in set2:
    set3.add(j)
print(set3)
print(set3.pop())
print(set3)
print(max(set3))
print(min(set3))
print(len(set3))
set4=set3.copy()
set4.add(11)
print(set4)
set1.clear()
set2.clear()
print(set1,set2)