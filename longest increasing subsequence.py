#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
   
    def lengthOfLIS(self, nums: List[int]) -> int:
        n , i = len(nums) , 1
        if len(nums) == 0: return 0
        dp = [1 for i in range(n)]
        for i in range(1 , n):
            j = 0
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
        return max(dp)

