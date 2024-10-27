Task      ## 27/10/24
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .


if __name__ == '__main__':
    n = int(input().strip())
    # if n % 2 != 0:
    #     print("Weird")
    # elif n % 2 == 0 & n > 2 & n <= 5:
    #     print("Not Weird")
    # elif n % 2 == 0 & n > 6 & n <= 20:
    #     print("Weird")
    # elif n % 2 == 0 & n > 20:
    #     print("Not Weird")
    if n%2 == 1: 
        print("Weird")

    else: # even value >> n is even 
        if n >2 and n <= 5: # number inclusive 2 to 5 
            print("Not Weird") 
        else: 
            if n > 6 and n <= 20: # number inclusive 6 to 20 
                print("Weird")
            else:
                print("Not Weird") # number greater then 20

