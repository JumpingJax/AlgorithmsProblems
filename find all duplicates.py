#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic={}
        for i in nums:
            dic[i]=0
        for i in nums:
            dic[i]+=1
        ret=[]
        
        for key,value in dic.items():
            if value>1:
                ret.append(key)
        return ret

