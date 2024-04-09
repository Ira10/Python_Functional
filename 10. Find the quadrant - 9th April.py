#!/usr/bin/env python
# coding: utf-8

# Find the quadrant
# Write a program that takes a point (x,y)
#  from the user and finds the quadrant where the point lies on a Cartesian plane.
# 
# The following illustration will help you to understand where each point lies on the Cartesian plane.

# ![Screenshot%202024-04-09%20at%207.33.03%E2%80%AFAM.png](attachment:Screenshot%202024-04-09%20at%207.33.03%E2%80%AFAM.png)

# In[2]:


x = int(input("Enter x "))
y = int(input("Enter y "))

if x > 0 and y > 0:
    print("The point lies in the 1st Quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the 2nd Quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the 3rd Quadrant.")
else:
    print("The point lies in the 4th Quadrant.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




