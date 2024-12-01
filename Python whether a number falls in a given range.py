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
