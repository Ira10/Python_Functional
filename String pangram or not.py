#######   11th Dec 

##### https://www.w3resource.com/python-exercises/python-functions-exercise-14.php

####  Note : Pangrams are words or sentences containing every letter of the alphabet at least once.


str_ =  "The quick brown fox jumps over the lazy dog"

vowel_ = {'a','e','i','o','u','#'}

if vowel_.issubset(set(str.lower(str_))):
    print("Panagram")
else:
    print("Not panagram")     ## Not panagram


# dict_ = {}

# print(set(str.lower(str_)))

# for i in set(str.lower(str_)):
    # if i in vowel_:
        # print("ab")
        # dict[i] += 1
    # else:
# print(dict_)


