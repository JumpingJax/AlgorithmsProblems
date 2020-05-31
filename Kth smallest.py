#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def helper(node,ls):
            if node:
                helper(node.left,ls)
                ls.append(node.val)
                helper(node.right,ls)
        lis=[]
        helper(root,lis)
        print(lis)
        return lis[k-1]  

