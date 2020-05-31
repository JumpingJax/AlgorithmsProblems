#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = set(nums) # remove duplicates
        d = dict(zip(x,[0]*len(x)))

        for num in nums:
	        for key in d.keys():  # go over each key to find if num < key then add +1 to corresponding key
		        if num<key:
			        d[key]+=1

        return [d.get(key) for key in nums]

