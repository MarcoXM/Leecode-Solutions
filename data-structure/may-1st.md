# may-1st/

1. **Merge Sorted Array**

   \`\`\`python class Solution: def merge\(self, nums1: List\[int\], m: int, nums2: List\[int\], n: int\) -&gt; None: """ Do not return anything, modify nums1 in-place instead. """

   ```text
   ## 正向遍历还需要O(M+N)空间
   ## 反向利用 nums1后面是0
   i = m - 1
   j = n - 1
   long_pointer = len(nums1) - 1
   while i>= 0 and j >= 0:
       if nums1[i] <= nums2[j]: # 保留席位
           nums1[long_pointer] = nums2[j]
           j -= 1
       else:
           nums1[long_pointer] = nums1[i]
           i -= 1
       long_pointer -= 1
   #nums1 原来的数字用完了
   nums1[:j + 1] = nums2[:j + 1]
   ```

```text
```go
func merge(nums1 []int, m int, nums2 []int, n int)  {
    i := m - 1
    j := n - 1
    p := len(nums1)-1
    for i >= 0 && j >= 0 {
        if nums1[i] <= nums2[j]{
            nums1[p] = nums2[j]
            j--
        } else {
            nums1[p] = nums1[i]
            i--
        }
        p--

    }
    for j >= 0 {
        nums1[p] = nums2[j]
        p--
        j--
    }

}
```

1. **Linked List Cycle**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next : return False
        # 套圈
        fast,slow = head,head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
```

```go
func hasCycle(head *ListNode) bool {
    if head == nil || head.Next == nil {
        return false
    }
    fast := head
    slow := head

    for fast.Next != nil && fast.Next.Next != nil {
        fast = fast.Next.Next
        slow = slow.Next
        if slow == fast {
            return true
        }
    }
    return false
}
```

1. **Intersection of Two Linked Lists**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_set = set()
        pA, pB = headA, headB
        while pB:
            node_set.add(pB)
            pB = pB.next

        while pA:
            if pA in node_set:
                return pA
            pA = pA.next
        return None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # linkedlist 相交肯定之多长为短链表.
        # 
        p1, p2 = headA, headB

        while p1 != p2:
            if p1 is not None :
                p1 = p1.next
            else:
                p1 = headB

            if p2 is not None:
                p2 = p2.next
            else:
                p2 = headA

            # 触发else的时候就是短的走完了,到长的走
            # 再触发保证等长

        return p1
```

