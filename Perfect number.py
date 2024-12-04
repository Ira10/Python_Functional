#####  4th Dec

### https://www.w3resource.com/python-exercises/python-functions-exercise-11.php#google_vignette

def perfect_():
    n = int(input())
    per = 0
    if n < 1:
        return "Not perfect"
    
    for x in range(1, n):
        if (n % x == 0):
            per += x 
    
    if per == n:
        return "Perfect"
    else:
        return "Not perfect"

print(perfect_())

# 28
# Perfect

# 4969
# Not perfect