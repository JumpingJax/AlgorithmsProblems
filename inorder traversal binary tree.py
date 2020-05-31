#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        liste=[]
        def rec(node,res):
            
            if node:
                
                rec(node.left,res)
                res.append(node.val)
                rec(node.right,res)
                
        rec(root,liste)
        return liste

