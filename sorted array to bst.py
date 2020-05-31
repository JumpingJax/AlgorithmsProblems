#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(ls):
            if not ls:
                return
            middle=len(ls)//2
            root=TreeNode(ls[middle])
            root.left=helper(ls[:middle])
            root.right=helper(ls[middle+1:])
            return root
        return helper(nums)

