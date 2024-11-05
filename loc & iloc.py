# pip install pandas
import pandas as pd
s = pd.Series(list("abcdef"), index=[49, 48, 47, 0, 1, 2]) 
# 49    a
# 48    b
# 47    c
# 0     d
# 1     e
# 2     f

print(s.loc[0])    # value at index label 0
# 'd'

print(s.iloc[0])  # value at index location 0
# 'a'

print(s.loc[0:1])  # rows at index labels between 0 and 1 (inclusive)
# 0    d
# 1    e

print(s.iloc[0:1]) # rows at index location between 0 and 1 (exclusive)
# 49    a