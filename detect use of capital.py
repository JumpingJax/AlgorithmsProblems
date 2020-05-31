#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        return word.isupper() or word.islower() or word.istitle()

