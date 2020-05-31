#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        p, q = headA, headB;
        while p != q:
            p = p.next if p else headB;
            q = q.next if q else headA;
        return p;

