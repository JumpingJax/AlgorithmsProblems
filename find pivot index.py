#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0: return -1
        if n==1: return 0
        left,right=0,sum(nums)
        for i in range(n):
            if left==right-(left+nums[i]):
                return i
            left+=nums[i]
        return -1

