########   4th Dec

#### https://www.w3resource.com/python-exercises/python-functions-exercise-8.php#google_vignette

def unique_list():
    lst = [int(item) for item in input("Enter numbers ").split(',')]
    # return set(lst)  ## {1, 2, 3, 4, 5}
    return list(set(lst))  # [1, 2, 3, 4, 5]

print(unique_list())

# Enter numbers 6,9,2
# [6, 9, 2]

# Enter numbers 1,2,3,4,5,1,2,3
# {1, 2, 3, 4, 5}

# Enter numbers 1,2,3,4,5,1,2,3
# [1, 2, 3, 4, 5]




# Define a function named 'unique_list' that takes a list 'l' as input and returns a list of unique elements
def unique_list(l):
    # Create an empty list 'x' to store unique elements
    x = []
    
    # Iterate through each element 'a' in the input list 'l'
    for a in l:
        # Check if the element 'a' is not already present in the list 'x'
        if a not in x:
            # If 'a' is not in 'x', add it to the list 'x'
            x.append(a)
    
    # Return the list 'x' containing unique elements
    return x

# Print the result of calling the 'unique_list' function with a list containing duplicate elements
print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))  
