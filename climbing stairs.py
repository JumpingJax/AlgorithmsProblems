#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def climbStairs(self, n: int) -> int:
        if n==2:
            return 2
        if n==3:
            return 3
        if n==1:
            return 1
        dp=[-1]*n
        dp[0]=1
        dp[1]=2
        
        for i in range(2,len(dp)):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[len(dp)-1]

