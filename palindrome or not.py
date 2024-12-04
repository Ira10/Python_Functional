#####  4th Dec
# https://www.w3resource.com/python-exercises/python-functions-exercise-12.php

def palindrome():
    n = input()
    if n == n[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome"

print(palindrome())

# madam
# Palindrome

# madamm
# Not palindrome