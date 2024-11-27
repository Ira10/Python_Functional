L = [1,2,3,'pi','#0',9,10,'r5']


try:
    for i in L:
        print(i/1)
except TypeError as e:
    print("Ooops, wrong type")

# 1.0
# 2.0
# 3.0
# Ooops, wrong type

print("\n")

for i in L:
    try:
        print(i/1)
    except TypeError as e:
        print("Ooops, wrong type")

# 1.0
# 2.0
# 3.0
# Ooops, wrong type
# Ooops, wrong type
# 9.0
# 10.0
# Ooops, wrong type

print(9/2)  ### 4.5
print(9//2) ## 4
print(9%2) ## 1