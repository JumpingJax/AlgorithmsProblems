#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# cheeky post order traversal we can just reverse the in order if we dont remember implementation
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        liste=[]
        def hel(node,res):
            if node:
                res.append(node.val)
                hel(node.right,res)
                hel(node.left,res)
        hel(root,liste)
        liste.reverse()
        return liste

