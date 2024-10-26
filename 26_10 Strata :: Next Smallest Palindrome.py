Given a number as an input, find the following smallest palindrome number. For simplicity, consider the upper limit of your search to be 1 million.


def next_palindrome(n):
    while True:
        n += 1
        if str(n) == str(n)[::-1]:  # Check if the number is a palindrome
            return n
    
