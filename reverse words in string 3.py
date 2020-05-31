#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        rev=[]
        for i in lst:
            rev.append(i[::-1])
        return " ".join(rev)

