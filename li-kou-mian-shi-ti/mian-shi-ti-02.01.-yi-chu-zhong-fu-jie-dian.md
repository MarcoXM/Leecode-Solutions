# 面试题 02.01. 移除重复节点

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        dit = {}
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while head:
            if head.val not in dit:
                pre.next = head
                dit[head.val] = 1
                head = head.next
                pre = pre.next
                
            else:
                head = head.next
            # print(dit)
        pre.next = None
        return dummy.next

        


```

