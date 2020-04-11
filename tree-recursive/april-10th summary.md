## april-10th 总结

1.所有的目的都是以为了增删查改.

23. **Merge k Sorted Lists**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        root = p = ListNode(0)       
        for node in sorted(nodes):
            p.next = ListNode(node)
            p = p.next
            
        return root.next
    
## 以上是个能做出来,但是不是及格的做法,因为linked list 本来就是,查询0(N),增删操作0(1)的结构.
## 以上的做法直接读取了value,然后整理,生成新list,浪费了linked list 本身的优良性质.并且直接改动val属于## 犯规操作,实际情况也不会直接改值,这样的做法令面试官challenge 你. 复杂度NlogN


## way 2 
## 保留linked 原来的结构才能更快,node.next 指向下一个node 无论这个node 是在什么container里面

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        h = [(head.val,i,head) for i,head in enumerate(lists) if head] # id 为了保证val 同值,能够比较.
        ## h 长度仅仅为K
        heapq.heapify(h) ## 对这些nodes 根据val排序, # 这步KlgK
        root = p = ListNode(-1)
        while h : # 这时 size 为 k
            ## 原理就是pop出来的node 连新链表
            _,idx, p.next = heapq.heappop(h)
            p = p.next
            if p.next:
                heapq.heappush(h,(p.next.val,idx,p.next))
        return root.next
            ##　 O(nklog(k)).

        
## 以上只是用了linked 的性质,并没有利用递归思想,简单说就是李永乐数据结构.
## 我们要找到独立的子问题, 我合并k条,就是 将 第kth 条和 merged k-1th 条合并.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def merge(l1, l2): ## merge 就是合并两个linked lists,照抄合并 2 sorted 
            p = head = ListNode(0) # dummy node
            while l1 or l2:
                if l1 and l2:
                    if l1.val <= l2.val:
                        p.next = l1
                        l1 = l1.next
                    else:
                        p.next = l2
                        l2 = l2.next
                    p = p.next

                elif not l1:
                    p.next = l2
                    break
                elif not l2:
                    p.next = l1
                    break        
            return head.next

        def divide(lists, start, end): ## end 是last idx 
            if start == end: ##[] 闭区间的好处表示单个元素
                return lists[start]
            mid = start + (end - start) // 2
            l1 = divide(lists, start, mid) ## 
            l2 = divide(lists, mid + 1, end)
            return merge(l1, l2)
        
        return divide(lists, 0, len(lists)-1) if lists else []
        



```



173. **Binary Search Tree Iterator**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    
    ## 本质就是inorder traverse 左中右 
    ## 最暴力就是将树变数组,然后用指针配合读取node.next()
    ## 但是空间复杂度 O(N),O(h)就已经提示了用stack了
    def __init__(self, root: TreeNode):
        self.stack = []
        self.root = root # root is none
    
    
    ### 要思考的是如果改中序遍历的模板
    ### 如果有root 就拼命放进去stack
    ### node none 就pop一个出来 重复循环 
    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.root: # 一开始是要放nodes 进stack 
            self.stack.append(self.root)
            self.root = self.root.left
        ## root ==None
        # print(self.stack ,"!!!")
        root = self.stack.pop()
        self.root = root.right # 设定新的root,遍历新的子树
        return root.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack or self.root: ##stack 有东西他就是下一个,如果stack没有,说不定没开始
            return True
        else:
            False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

**Closest Binary Search Tree Value I**

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        
        ## 这就是中序!
        ## 暴力 变array 然后比大小
        ## 这样的缺点是要先遍历完 完完完完完 整棵树 
        ## 这就浪费了树的特点了
        self.ans = root.val
        def helper(root,min_dis):
            if not root:
                return
            if abs(root.val - target)  < min_dis: # 操作
                self.ans = root.val
                min_dis = abs(root.val - target)
                
            ## 遍历
            helper(root.left,min_dis)
            helper(root.right,min_dis)
            
        
        helper(root,abs(root.val - target))
        return self.ans  
    ## 明明算法是对的,但是修改值的话,还是吧值变成self.吧.
    ## 这个就是最简单的遍历
    
    	## 遍历更好的 利用bst遍历
            if target < root.val:
                helper(root.left,min_dis)
            else:
                helper(root.right,min_dis)
                
                
## 至下而上的递归
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        ans = root.val ##
        if target < ans:
            root = root.left
        else:
            root = root.right
        if not root :
            return ans
        ans2 = self.closestValue(root,target)
        return ans if abs(ans - target) < abs(ans2 - target) else ans2

                
            
        
        
```



901. **Closest Binary Search Tree Value II**

```python

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        ## 最暴力,中序遍历,然后iterate出来结果,这个就算了.
        ## 复杂度0(N)
        
        ## 接下来就是在遍历的过程中优化,维护一个size为K的container
        ## 遍历iterate 就用 stack, 递归就明显比迭代复杂
        ## 默写 inorder 代码
        
        ans = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        print(ans)
            
            
            
     ##中间的container可以用别的 KlogN
 		self.ans = []
        def inorder(root,target,k):
            if not root:
                return
            inorder(root.left,target,k)
            if len(self.ans) >= k :
                if abs(root.val - target) <  abs(self.ans[0] - target):
                    self.ans = self.ans[1:]
                    self.ans.append(root.val)
                else:
                    return
            else: # 直接加啦
                self.ans.append(root.val)
            inorder(root.right,target,k)
        
        inorder(root,target,k)
            
        return self.ans
    
    
    ##lgN + K.就是找到最值,左右横移动,怀念数组
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        ## 最暴力,中序遍历,然后iterate出来结果,这个就算了.
        ## 复杂度0(N)
        
        ## 接下来就是在遍历的过程中优化,维护一个size为K的container
        ## 遍历iterate 就用 stack, 递归就明显比迭代复杂
        ## 默写 inorder 代码
    
        ## 添加参数
        
        pre_nodes = [] # 在查找的过程中你是逼近target的所以后入stack的元素离得近
        later_nodes = []
        ans = []
        while root:
            if root.val < target:
                pre_nodes.append(root)
                root = root.right
                
            else :
                later_nodes.append(root) #千万不要破tree结构
                root = root.left
        ### 到底了
        
        while k > 0:
            ## 分别为对面没有 或者是两者都有
            if (not later_nodes and pre_nodes) or (later_nodes and pre_nodes and target - pre_nodes[-1].val  < later_nodes[-1].val - target):
                ans.append(pre_nodes[-1].val)
                self.renew_pre(pre_nodes)
                
            elif (later_nodes and not pre_nodes) or (later_nodes and pre_nodes and target - pre_nodes[-1].val  > later_nodes[-1].val - target):
                ans.append(later_nodes[-1].val)
                self.renew_later(later_nodes)
            k -= 1
        return ans
        
        
    def renew_pre(self,pre_nodes): #镜像对称
        node = pre_nodes.pop()
        if node.left:
            pre_nodes.append(node.left)
            while pre_nodes[-1].right:
                pre_nodes.append(pre_nodes[-1].right)
        
        
    def renew_later(self,later_nodes):
        node = later_nodes.pop()
        if node.right:
            later_nodes.append(node.right)
            while later_nodes[-1].left:
                later_nodes.append(later_nodes[-1].left) ##镜像对称
        
        
```

