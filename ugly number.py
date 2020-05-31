#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        arr = {2,3,5}
        while num > 1:
            for n in arr:
                if num%n == 0:
                    num = num//n
                    break
            else:
                return False
        return True

