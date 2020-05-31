#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.check(s,t) and self.check(t,s)
        
    def check(self, s,t):
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=t[i]
            elif dic[s[i]]!=t[i]:
                return False
        return True

