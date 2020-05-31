#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# use backtracking algorithm when wanting all possible combinations or ways of doing something
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result = []
        def backtrack(l,r,nums):
            if l==r :
                return result.append(list(nums)) #We reached the end of the recursion
                                                 #tree
            else: 
                for i in range(l,r+1):
                    # swap then call recursively then switch back to what it was
                    nums[l], nums[i] = nums[i], nums[l]
                    backtrack(l+1,r,nums)
                    nums[i],nums[l] = nums[l], nums[i]
        backtrack(0,n-1,nums)
        return result

