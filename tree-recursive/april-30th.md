### april-30th

121. **Best Time to Buy and Sell Stock**

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        h = []
        profit = 0
        for price in prices:
            heapq.heappush(h,price) # 永远找到之前的最低价格
            profit = max(profit, price - h[0])
        return profit 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        minrice = float('inf')
        profit = 0
        for price in prices:
            min_rice = min(minPrice, price)
            profit = max(profit, price - min_rice)
        return profit
```

```go
func maxProfit(prices []int) int {
    var profit int
    min_price := 1<<31 - 1
    for _,v := range prices {
        min_price = min(v,min_price)
        profit = max(profit, v-min_price)
    }
    return profit
}

func min(a int, b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}

func max(a int, b int) int {
    if a < b {
        return b
    } else {
        return a
    }
}
```





106. **Construct Binary Tree from Inorder and Postorder Traversal**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        ## 首先这是有规律的 p 最后是root 
        ## 这里recursion传递的变量 本身的函数不够,其实是可以的,但是传递array 可能会超内存所以helper
        ## p 最后就是root, root 元素的左边就是left,右边就是right
        
        if not inorder or len(inorder)== 0 :
            return 
        
        def build(l, r):
            if l > r: # 终止条件
                return None
            
            ## 建树的遍历顺序,先root 儿子
            v = postorder.pop() # 最后一位
            root = TreeNode(v)
            index = inorder.index(v) # 优化 空间换时间non-index
            
            root.right = build(index+1,r) # 用的是pop post 所以要right first
            root.left = build(l,index-1) # 前一个就是left
            return root
        
        return build(0,len(inorder)-1)
    
        
```

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(inorder []int, postorder []int,) *TreeNode {
    if len(postorder) == 0 || len(inorder) == 0 {
        return nil
    }

    // 找根节点, go lang 风格用range
    var idx int
    for k, v :=  range inorder {
        if v == postorder[len(postorder) - 1] {
            idx = k
            break
        }
    }

    // Divided
    // post_left, post_right := postorder[0: idx], postorder[idx: -1]
    // in_left, in_right := inorder[0: idx], inorder[idx+1:]
    
    // 左右子树递归,不太熟指针的话,还是认怂,不传idx.
    return &TreeNode{
        Val:   postorder[len(postorder)-1],
        Left:  buildTree(inorder[0: idx], postorder[0: idx]),
        Right: buildTree(inorder[idx+1:], postorder[idx:len(postorder)-1]),
    }
}

```



105. **Construct Binary Tree from Preorder and Inorder Traversal**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        ###
        ## 和上题相比就是post 变成了pre
        ## 还是找规律
        ## pre 开头就是 root
        ## inorder 性质不变 
        
        if not preorder or len(inorder)==0:
            return 
        
        def build(l, r ):
            
            if l > r:
                return None # 照抄
            root = TreeNode(preorder.pop(0))
            index = inorder.index(root.val)
            root.left = build(l,index - 1)
            root.right = build(index + 1,r)
            return root
        
        return build(0,len(inorder)-1)
```

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(preorder) == 0 || len(inorder) == 0 {
        return nil
    }

    // 找根节点, go lang 风格用range
    var idx int
    for k, v :=  range inorder {
        if v == preorder[0] {
            idx = k
            break
        }
    }

    // Divided
    // pre_left, pre_right := preorder[1: idx+1], preorder[idx+1:]
    // in_left, in_right := inorder[0: idx], inorder[idx+1:]
    
    // 左右子树递归,不太熟指针的话,还是认怂,不传idx.
    return &TreeNode{
        Val:   preorder[0],
        Left:  buildTree(preorder[1: idx+1], inorder[0: idx]),
        Right: buildTree(preorder[idx+1:], inorder[idx+1:]),
    }
}

```

