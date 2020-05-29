#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# uses hashtable to count frequency of elements for each element
# removes that element until only 1 remains
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dic={}
        for i in nums:
            dic[i]=0
        for i in nums:
            dic[i]+=1
        for i in nums:
            if dic[i]>1:
                while dic[i]>1:
                
                    nums.remove(i)
                    dic[i]-=1

