#!/usr/bin/env python
# coding: utf-8

# In[1]:


c , d = 5 , 6
print (c , d)


# In[2]:


a = input ()
b = input ()
print (a+b)


# In[3]:


int1 = 19
int2 = 4
print (int1 / int2)


# In[4]:


num1 = 19
num2 = 4
num1 %= num2
print (num1 , num2)


# In[5]:


num3 = 3
num4 = 2
num3 **= num4
print (num3 , num4)


# In[6]:


num5 = 5
num6 = 6
num5 //= num6
print (num5 , num6)


# In[7]:


a = b = 34
print (a , b)


# In[10]:


a = 8
if a > 0:
    print("Positive ",end="")
    if a % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative")


# In[11]:


a, b = 12, 5
if a >= b:
    print('True')
else:
    print('False')


# In[12]:


dividend = 12
divisor = 0
print(dividend)
quotient = dividend / divisor
print(quotient)

