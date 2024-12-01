########  23rd Nov

## https://www.w3resource.com/python-exercises/python-functions-exercise-6.php 

# def range_check(n, range_start, range_end):
# #     n = int(input("Enter the n "))
# #     range_start = int(input("Enter the starting "))
# #     range_end = int(input("Enter the ending "))

#     # while n>= range_start or n <= range_end:
#     if n == range_start or n == range_end:
#         print("n is present")
        
#     elif (range_end + range_start) / 2 <= n: #### not correct
#         print("n is present")

#     else:
#         print("n is not present")
# # return None

# n = int(input("Enter the n "))
# range_start = int(input("Enter the starting "))
# range_end = int(input("Enter the ending "))

# print(range_check(n, range_start, range_end))

print(abs(11/2))


# Enter the n 6
# Enter the starting 22
# Enter the ending 24
# n is present
# None
# 5.5


# Enter the n 110
# Enter the starting 1
# Enter the ending 98
# n is present
# None
# 5.5



def range_check(n, range_start, range_end):
#     n = int(input("Enter the n "))
#     range_start = int(input("Enter the starting "))
#     range_end = int(input("Enter the ending "))

    # while n>= range_start or n <= range_end:
    if range_start <= n <= range_end:
        print("n is present")

    else:
        print("n is not present")
# return None

n = int(input("Enter the n "))
range_start = int(input("Enter the starting "))
range_end = int(input("Enter the ending "))

print(range_check(n, range_start, range_end))


##############################################

# Define a function named 'test_range' that checks if a number 'n' is within the range 3 to 8 (inclusive)
def test_range(n):
    # Check if 'n' is within the range from 3 to 8 (inclusive) using the 'in range()' statement
    if n in range(range_start, range_end):
        # If 'n' is within the range, print that 'n' is within the given range
        print("%s is in the range" % str(n))
    else:
        # If 'n' is outside the range, print that the number is outside the given range
        print("The number is outside the given range.")

# Call the 'test_range' function with the argument 5
test_range(n)



# 5.5
# Enter the n 5
# Enter the starting 11
# Enter the ending 17
# n is not present
# None
# The number is outside the given range.

