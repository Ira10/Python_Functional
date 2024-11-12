####### 12th Nov 
#### https://www.w3resource.com/python-exercises/python-functions-exercises.php -- 3


# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336


### 1. Use 'Reduce' function

import functools

L = [8, 2, 3, -1, 7]

def list_mult(L): 
    product = functools.reduce(lambda x, y: x * y, L)
    return product

print(list_mult(L))



##### 2. Using 'for'

def list_multi(L):
    product_ = 1 
    for i in L:
        product_ *= i 
    return product_

print(list_multi(L))



###### 3. Using numpy 

import numpy
list = [8,2,3,-1,7]

result = numpy.prod(list)
print(result)
# Output:-336