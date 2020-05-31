#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        maxnum=max(nums)
        maxind=nums.index(maxnum)
        nums.pop(maxind)
        newmax=max(nums)
        if maxnum>=2*newmax:
            return maxind
        return -1

