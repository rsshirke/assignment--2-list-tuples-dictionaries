#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples



# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for index in range(0, len(my_list)): 
          for next_index in range(0, len(my_list)-index-1): 
            if (my_list[next_index][1] > my_list[next_index + 1][1]): 
                temp = my_list[next_index] 
                my_list[next_index]= my_list[next_index + 1] 
                my_list[next_index + 1]= temp 
print(my_list)


# # Question2

# In[2]:


# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

# Sample Output : {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}

my_dict = {chr(i): i for i in range(ord('a'),ord('z')+1)}
print(my_dict)


# In[ ]:




