#### 12th Nov

### https://www.w3resource.com/python-exercises/python-functions-exercises.php -- 4

# Sample String : "1234abcd"
# Expected Output : "dcba4321"

s = '1234abcd'
name = 'Indrani Sarkar'

print(s[::-1])   ### dcba4321
print('\n')
print(name[::-1])   #### rakraS inardnI
print(name[::1]) 


# print(a[2:-1])

# The slice a[2:-1] accesses elements from index 2 up to (but not including) -1.
# Index 2 corresponds to 3, and -1 refers to 6. Since the end index is non-inclusive, it stops before 6.
# This slice therefore includes [3, 4, 5].
# Output: [3, 4, 5]


##############################################
# The [::-1] slice in Python reverses a list, string, or any other sequence.

# Here's how it works:

# The slicing syntax [start:end:step] allows you to specify a start index, an end index, and a step (or stride) for the slicing.
# When you use [::-1], you are saying:
# Start from the end of the list (since no start index is specified, it defaults to the end).
# End at the beginning of the list (since no end index is specified, it defaults to the beginning).
# Step backward by -1.





# Let’s clarify how slicing works, especially when specifying only the step value, such as `[::1]` or `[::-1]`. The rules can be a bit confusing at first, but here’s how it actually works:

# ### Key Points for Slicing `[start:end:step]`

# 1. **If `start` is not specified**:
#    - It defaults to the beginning of the sequence (`0`) if `step` is positive.
#    - It defaults to the end of the sequence if `step` is negative.

# 2. **If `end` is not specified**:
#    - It defaults to the end of the sequence if `step` is positive.
#    - It defaults to the beginning of the sequence if `step` is negative.

# 3. **Step**:
#    - A positive step moves from the start index to the end index.
#    - A negative step moves from the start index to the end index in reverse.

# ### How These Rules Apply to `[::1]` and `[::-1]`

# #### Case 1: `[::1]`
# - `start` is not specified, so it defaults to the beginning of the sequence.
# - `end` is not specified, so it defaults to the end of the sequence.
# - `step` is `1`, meaning we go forward from `start` to `end` without reversing or skipping.

#    So, `[::1]` gives you a copy of the entire sequence from start to end in the original order.

# #### Case 2: `[::-1]`
# - `start` is not specified, so it defaults to the end of the sequence.
# - `end` is not specified, so it defaults to the beginning of the sequence.
# - `step` is `-1`, meaning we go backward from `start` to `end`.

#    This effectively reverses the sequence because we start from the end and move backward one element at a time until we reach the beginning.

# ### Examples

# ```python
# a = [1, 2, 3, 4, 5]

# # [::1] - Copies the list as is
# print(a[::1])  # Output: [1, 2, 3, 4, 5]

# # [::-1] - Reverses the list
# print(a[::-1])  # Output: [5, 4, 3, 2, 1]
# ```

# ### Why `[::1]` Doesn’t Start from the End

# The confusion might be because of how the defaults work with positive and negative steps. Here’s a summary:

# - For **positive steps**, slicing moves forward (from beginning to end by default).
# - For **negative steps**, slicing moves backward (from end to beginning by default).

# So, `[::1]` defaults to a forward direction, while `[::-1]` defaults to a reverse direction, explaining the difference in behavior.
