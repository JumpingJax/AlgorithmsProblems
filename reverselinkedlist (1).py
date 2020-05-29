#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# essentially draw out a linked list and point all of the arrows in the opposite direction
# translate that drawing into code
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur=head
        prev=None
        nex=None
        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        head=prev
        return head

