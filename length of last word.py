#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_len = 0
        for char in reversed(s):
            if char != " ":
                last_len += 1
            elif last_len > 0:
                break
        return last_len 

