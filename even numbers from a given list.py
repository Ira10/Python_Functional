### 4th Dec

## https://www.w3resource.com/python-exercises/python-functions-exercises.php

def even_num():
    lst = [int(item) for item in input("Enter numbers ").split(',')]
    return [i for i in lst if i%2==0]

print(even_num())

#Enter numbers 1, 2, 3, 4, 5, 6, 7, 8, 9
# [2, 4, 6, 8]
