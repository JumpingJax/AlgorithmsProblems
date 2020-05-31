#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ls=[]
        def helper(node,ls):
            if node:
                helper(node.left,ls)
                ls.append((node.val))
                helper(node.right,ls)
        helper(root,ls)
        if  ls==sorted(ls) and len(ls)==len(set(ls)):
            return True
        return False

