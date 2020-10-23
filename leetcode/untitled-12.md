# Untitled

{% tabs %}
{% tab title="" %}
```

```
{% endtab %}

{% tab title="Python" %}
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
## 本能做法 ！
        if not head :
            return True

        ans = []
        while head:
            ans.append(head.val)
            head = head.next

        return ans == ans[::-1]
```
{% endtab %}
{% endtabs %}

