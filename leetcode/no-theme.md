# 23. Merge k Sorted Lists

{% tabs %}
{% tab title="Python" %}
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        
        return self.divide(lists, 0, len(lists))
        
        
    def divide(self, lists, left , right):
        if left == right - 1:
            return lists[left]
        mid = left + right >> 1
        l1 = self.divide(lists, left, mid)
        l2 = self.divide(lists, mid, right)
        return self.merge(l1, l2)
        
        
    def merge(self, a, b):
        if not a and not b:
            return 
        dummy = ListNode(-1)
        node = dummy 
        while a and b:
            if a.val <= b.val:
                node.next = a
                a = a.next
            else:
                node.next = b
                b = b.next
            node = node.next
            
        if not a:
            node.next = b
        if not b:
            node.next = a
            
        return dummy.next
        
```
{% endtab %}

{% tab title="分治" %}
```python
##分治　
##我们做完第一题已经有治了，　现在就只要关心怎么分
# N*log(K)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        return self.divide(lists,0 , len(lists))
        
    def divide(self,lists, left, right):
        if left == right - 1:
            return lists[left]
        mid = (right + left)//2
        l1 = self.divide(lists,left,mid)
        l2 = self.divide(lists,mid,right)
        return self.mergeTwoLists(l1, l2)
    
    ### 照抄
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return 
        dummy = ListNode(-1)
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next
                
        if l1:
            head.next = l1
        else:
            head.next = l2
            
        return dummy.next
```
{% endtab %}

{% tab title="Heap" %}
```python
## 这题可以怎么看考。。
## 分治，结合上面的合并两个list。 我个人觉得 分治比较符合这题出的本意。 
## heap 的话 没有必要出这一题
##　先写简单的


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# N*log(K)

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(-1)
        head = dummy
        ## 主要是使用heap code就会简明很多 
        ## 要处理的是如何可以在pop了对应的node以后，push 它的next
        
        hp = [(node.val,idx, node) for idx,node in enumerate(lists) if node]
        heapq.heapify(hp)
        while hp:
            _ ,idx ,node = heapq.heappop(hp)
            head.next = node
            head = head.next
            if node.next:
                heapq.heappush(hp,(node.next.val,idx,node.next))
        
        return dummy.next
## 这个其实也是迭代 
```
{% endtab %}
{% endtabs %}

