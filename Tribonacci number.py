#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def helper(n):
            if n==0:
                return 0
            if n==1 or n==2:
                return 1
            if n in memo:
                return memo[n]
            if n not in memo:
                result=helper(n-1)+helper(n-2)+helper(n-3)
                memo[n]=result
            return result
        return helper(n)

