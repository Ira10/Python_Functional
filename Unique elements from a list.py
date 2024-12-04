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