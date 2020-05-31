#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic={}
        for i in arr:
            dic[i]=0
        for i in arr:
            dic[i]+=1
            
        for key,value in dic.items():
            if value>1/4*len(arr):
                return key

