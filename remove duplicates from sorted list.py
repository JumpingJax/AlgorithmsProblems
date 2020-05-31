#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# this could be done without storing values since we know it should be increasing we just remove if we find two equal elements
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        if head == None:
            return head
        alist = []
        alist.append(head.val)
        
        while(current.next):
            if current.next.val in alist:
                current.next = current.next.next
            else:    
                current = current.next
                alist.append(current.val)
        return head

