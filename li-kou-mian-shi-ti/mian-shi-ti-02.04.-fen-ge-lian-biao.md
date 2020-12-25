# 面试题 02.04. 分割链表

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        dummy = ListNode(-1)
        f = g  = ListNode(-1)
        node = head 
        dummy.next = head 
        pre = dummy
        while node:
            if node.val < x:
                pre.next = node
                pre = pre.next

            else :
                g.next = node
                g = g.next

            node = node.next
        g.next = None
        pre.next = f.next
        return dummy.next 
```

