def num_in_range(num,min,max):
    if num in range(min,max+1):
        return True
    else:
        return False
print(num_in_range(8,1,12))