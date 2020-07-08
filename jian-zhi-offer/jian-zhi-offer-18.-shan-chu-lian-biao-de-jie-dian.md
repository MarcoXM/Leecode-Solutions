# 剑指 Offer 18. 删除链表的节点

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, root: ListNode, val: int) -> ListNode:
     ### 还是要多画图.. 不然久了不做会坑
        dummy = ListNode(-1)
        dummy.next = root
        head = dummy
        while head.next and head.next.val != val:
            head = head.next
        
        if head.next:
            head.next = head.next.next

        return dummy.next
```

