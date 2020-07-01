# may-18th

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## 滑動窗口.. 我不知道爲什麼變成了繁體字,
        ##
        l = 0
        r = 0
        s1hash = {k : s1.count(k) for k in s1} 
        s2hash = collections.defaultdict(int)
        match = 0

        while r < len(s2):
            word = s2[r]
            if word in s1hash.keys():
                s2hash[word] += 1
                if s2hash[word] == s1hash[word]:
                    match += 1
            r += 1

            ## 窗口內元素符合
            while match == len(s1hash):
                ## 長度符合 
                if r - l == len(s1):
                    return True
                ## 更新 同上 
                word2 = s2[l]
                if word2 in s1hash.keys():
                    s2hash[word2] -= 1
                    if s2hash[word2] < s1hash[word2]:
                        match -= 1
                l += 1
        return False
    ## On 額外空間(26)
```

```python
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the product list of l1 and l2
    """
    def multiplyLists(self, l1, l2):
        # write your code here

        return self.toInt(l1) * self.toInt(l2)

    def toInt(self,head):
        res = 0
        while head:
            res = res * 10
            res += head.val
            head = head.next
        return res
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ##　分類討論
        ans = ListNode(-1) # 假頭
        node = ans
        flag = 0

        while l1 and l2:
            val = l1.val + l2.val + flag 
            flag = val//10
            val = val%10
            node.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            node = node.next

        while l1 and not l2:
            val = l1.val + flag
            flag = val//10
            val = val%10
            node.next = ListNode(val)
            l1 = l1.next
            node = node.next

        while not l1 and l2:
            val = l2.val + flag
            flag = val//10
            val = val%10
            node.next = ListNode(val)
            l2 = l2.next
            node = node.next

        if flag == 1:
            node.next = ListNode(flag)
        return ans.next
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ##　分類討論,字少
        ans = ListNode(-1) # 假頭
        node = ans
        value = 0
        while l1 or l2:
            if l1:
                value += l1.val
                l1 = l1.next

            if l2:
                value += l2.val
                l2 = l2.next
            node.next = ListNode(value%10)
            value //= 10
            node = node.next

        if value == 1:
            node.next = ListNode(value)
        return ans.next
```

