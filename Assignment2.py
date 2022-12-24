#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

# In[ ]:


l= [(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i][1]<l[j][1]:
            l[i],l[j]=l[j],l[i]
print("Expected Result:",l)


# # Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

# In[ ]:


ascii_list=[]
alpha_list=[]

for num in range(97,123):
    ascii_list.append(num)
for num in ascii_list:
    alpha_list.append(chr(num))


print("sample output:",alpha_list,ascii_list)

