#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            dic[i]=0
        for i in nums:
            dic[i]+=1
        for key,value in dic.items():
            if value==1:
                return key

