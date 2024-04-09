#!/usr/bin/env python
# coding: utf-8

# This program should calculate the pay of an employee based on hours worked. The input includes the employee’s total hours worked per week and their hourly pay rate. The employee will be paid a base wage for the first 40 hours worked and time-and-a-half (150% of base pay) for any hours past 40 as overtime pay. Output the regular pay, overtime pay, and total pay for the week on the screen.
# 
# If the employee worked 40 hours or less, don’t show any output regarding overtime pay.
# 
# 

# In[3]:


hour = int(input("Enter how many hours worked "))
pay = int(input("Enter the hourly rate "))

if hour < 40:
    print("No overtime pay ")
    print(hour*pay)
elif hour > 40:
    reg_pay = 40 * pay
    overtime_hour = hour - 40
    overtime_pay = overtime_hour * pay * 150%
    total_pay = reg_pay + overtime_pay
    print("reg_pay \n")
    print("overtime_pay \n")
    print("total_pay \n")


# In[5]:


hour = int(input("Enter how many hours worked "))
pay = int(input("Enter the hourly rate "))

if hour < 40:
    print("No overtime pay ")
    print(hour*pay)
elif hour > 40:
    reg_pay = 40 * pay
    overtime_hour = hour - 40
    overtime_pay = overtime_hour * pay * 1.5
    total_pay = reg_pay + overtime_pay
    print("reg_pay \n", reg_pay)
    print("overtime_pay \n", overtime_pay)
    print("total_pay \n", total_pay)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




