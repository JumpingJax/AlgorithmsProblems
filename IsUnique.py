#!/usr/bin/env python
# coding: utf-8

# In[24]:


# isUnique
# Implement an algorithm to determine if a string has all unique characters. We return False if it has not all unique characters, True if unique
# First we have a few edge cases (assume not counting whitespace as a character)
# if a string has more than 26+10 characters a-z & 0-9 then it cannot be unique

# O(n) solution
def isUnique(string):
    if len(string)>36:
        return False
    if len(string)==1 or len(string)==0:
        return True
    # we can use a hashtable to keep count of each character
    dic={}
    for i in string:
        dic[i]=0
    for i in string:
        dic[i]+=1
    for key,value in dic.items():
        if value==2:
            return False
    return True
# Alternatively if we cannot use an additional data structure
def isUnique2(string):
    if len(string)>36:
        return False
    if len(string)==1 or len(string)==0:
        return True
    # for each element in our array we can search for the duplicate in a partitioned string such that we dont include that indice
    for i in range(len(string)):
        if string[i] in string[i+1:] or string[i] in string[:i]:
            return False
    return True



# In[23]:


string='123456'

print(string[:3])
print(string[3+1:])


# In[ ]:




