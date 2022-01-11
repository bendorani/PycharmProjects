def polinorm(str1:str):
    str2=""
    for i in str1:
        if i!=" ":
            str2+=i

    if str2==str2[::-1]:
        return True
    else:
        return False

str1="nurses run"
str2="abcdefg"
print(polinorm(str1))
print(polinorm(str2))