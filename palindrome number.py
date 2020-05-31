#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringlist=list(str(x))
        stringlist.reverse()
        if ''.join(stringlist)==str(x):
            return True
        return False

