# 面试题 02.02. 返回倒数第 k 个节点

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:

        l = 0
        node = head
        while node:
            l += 1
            node = node.next

        while l - k:
            head = head.next
            l -= 1

        return head.val


        
```

