#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Check palindrome question
def check_pal(str1,str2):
    return reverse_string(str1)==str2
def reverse_string(string):
    if len(string)==0:
        return ''
    return reverse_string(string[1:])+string[0]


# In[7]:


# Check permutation question
def check_perm(str1,str2):
    if len(str1)!=len(str2):
        return False
    # count characters see if count for character in either string differs
    dic1={}
    dic2={}
    for i in dic1:
        dic1[i]=0
    for i in dic1:
        dic1[i]+=1
    for i in dic2:
        dic2[i]=0
    for i in dic1:
        dic2[i]+=1
    for key,value in dic1.items():
        if key not in dic2:
            return False
        if key in dic2:
            if dic1[key]!=dic2[key]:
                return False
    return True
print(check_perm('abc','bcab'))


# In[ ]:




