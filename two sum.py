#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Two sum problem
# this is a lookup problem use hashtable to keep track of indices and if target-any given nums is in dicta or not
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicta={}
        for i in range(len(nums)):
            dicta[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in dicta:
                if dicta[target-nums[i]]!=i:
                    return [i,dicta[target-nums[i]]]

