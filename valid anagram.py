#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s)==Counter(t)

