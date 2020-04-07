# april-1st

1. **Rotate Image**

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ## 这个因为in-place 不能一步到位.
        ## 顺时针rotation 等价于 先xy坐标互换,再每行翻转,节省空间总是浪费时间
        N = len(matrix)
        for i in range(N):
            for j in range(i,N): # Transpose 不能全遍历
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]

        # 翻转行
        for i in range(N):
            matrix[i].reverse()

      # O(N^2)
```

1. **Remove Linked List Elements**

```python
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return 

        root = ListNode(0)
        root.next = head
        cur = root
        while cur.next: # 判断下一个,如果我们判断现在所在的node,我们要跳过本node,又要多一个指针
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return root.next

    # 0(N)
```

1. **Swap Nodes in Pairs**

```python
## iterative 
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = ListNode(0)
        root.next = head
        cur = root
        while cur.next and cur.next.next:
            # curr > a > b > b.next  >>>>> cur > b > a > b.next
            a = cur.next
            b = a.next

            cur.next = b
            a.next = b.next
            b.next = a

            # update cur
            cur = a

        return root.next

    # O(N)
```

```python
## recursive 
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head and not head.next:
            return head

        a = head
        b = head.next 

        # a 要挪到后面 就是剩下的
        a.next = self.swapPairs(b.next)
        b.next = a # 接上新头

        return b 
    # O(N)
```

1. **Pow\(x, n\)**

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ## Intuitive 
        return x**n
    ## O(N)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ## 分类讨论
        ## Corner Case
        if n == 0:
            return 1
        elif n < 0:
            ## 
            x = 1/x
            n = -n      

        if n%2 ==0:
            return self.myPow(x**2,n//2) # 乘子翻倍 
        return x*self.myPow(x,n-1) # 减1 然后变成偶数个
    ## O(logN)
```

\450. **Delete Node in a BST**

```python
## Recursive 
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        ## 左儿子 比自己小, 右儿子比自己大
        ## iterative 
        ## Corner Case
        if not root:
            return 

        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            ## 上面就是简单的情况

            if root.left and root.right:
                # 我们的原则是找,左边的最大的
                lnode = root.left
                if not lnode.right: #一开始就不能再往右边走,所以返回左儿子
                    lnode.right = root.right
                    return lnode
                ## 当右儿子一直有的时候,一直找,保留当前node
                while lnode.right:
                    pre = lnode
                    lnode = lnode.right # 一直找找到最大的
                ## 找不下去了,看看有没它的 左儿子
                pre.right = lnode.left
                lnode.right = root.right #这个lnode 成为了新的ｒｏｏｔ
                lnode.left = root.left
                return lnode
        # BFS
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)

        return root


## iterative  
## 树真的是天配recursion
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        ## iterative 
        ## Corner Cas
        if not root:
            return 
        # 不会
        pass 

##Follow Up 追问,key 变成top K
##
class Solution:
    def deleteNode(self, root, key):
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        K = inorder(root)[-key] # 将top k装换为值
```

1. **Validate Binary Search Tree**

```python
## Recursive 

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        return self.helper(root,-2**32,2**32)

    def helper(self,root,min,max):
        if not root:
            return True
        if root.val >= max or root.val<=min:
            return False

        return self.helper(root.right,root.val,max) and self.helper(root.left,min,root.val)
    # O(n)



## Iterative

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = []
        pre = None  
        while root or stack != []:
            while root:
                stack.append(root)
                root = root.left # 左儿子,一直狂塞，到最左边
                # print(stack)
            root = stack.pop() # 全场最小，inorder 就是单调递增
            if pre!= None and pre.val >= root.val:
                return False
            pre = root
            root = root.right
        return True
```

1. **Split a String in Balanced Strings**

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s:
            return 0 # corner case
        ans = 0
        from collections import defaultdict
        dit = defaultdicｔ(int)
        for i in range(len(s)):
            if s[i] == "R":
                dit["R"] +=1
            elif s[i] =="L":
                dit["L"] +=1
            if dit["R"] == dit["L"]:
                ans += 1
                dit["R"] = 0
                dit["L"] = 0
        return ans
    # O(N)
```

