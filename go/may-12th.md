## may-12th

\236. Lowest Common Ancestor of a Binary Tree

```go

/**
 * Definition for TreeNode.
 * type TreeNode struct {
 *     Val int
 *     Left *ListNode
 *     Right *ListNode
 * }
 */
 func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
  
     // 原function 就是return node的
     if root == nil{
         return root
     }
     if root == p || root == q {
        return root
    }
     // 剩下就是root 有 且不为孩子
     left := lowestCommonAncestor(root.Left, p, q)
     right := lowestCommonAncestor(root.Right, p, q)
     
     if left != nil && right != nil{
         return root
     }else if left != nil && right == nil{
         return left
     }
     return right
     
}

  /**
 * Definition for TreeNode.
 * type TreeNode struct {
 *     Val int
 *     Left *ListNode
 *     Right *ListNode
 * }
 */
 func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
     if root == nil || p == nil || q == nil {
         return nil
     }
     pathQ := getPath(root,q)
     pathP := getPath(root,p)
     var ans *TreeNode
     
     for i := 0 ; i < len(pathQ) && i < len(pathP);i++ {
         if pathQ[i].Val == pathP[i].Val {
             ans = pathQ[i] 
         } else {
            break
         }
     }
     return ans
          
 }
func getPath(root, n *TreeNode) []*TreeNode {
    s := make([]*TreeNode,0)
    var lastVisited *TreeNode
    for s != nil || root != nil {
        if root != nil {
            s = append(s,root)
            root = root.Left
        } else {
            node := s[len(s)-1]
            if node.Right != nil && lastVisited != node.Right {
                root = node.Right
            } else {
                if node == n {
                    return s
                }
                lastVisited = s[len(s)-1]
                s = s[:len(s)-1]
                root = nil
            }
        }
        
    }
    return s
}



/**
 * Definition for TreeNode.
 * type TreeNode struct {
 *     Val int
 *     Left *ListNode
 *     Right *ListNode
 * }
 */

// 熟悉指针操作.从OJ来看性能无差异
 func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
     if root == nil || p == nil || q == nil {
         return nil
     }
     pathQ := getPath(root,q)
     pathP := getPath(root,p)
     var ans *TreeNode
     
     for i := 0 ; i < len(*pathQ) && i < len(*pathP);i++ {
         if (*pathQ)[i].Val == (*pathP)[i].Val {
             ans = (*pathQ)[i] 
         } else {
            break
         }
     }
     return ans
          
 }
func getPath(root, n *TreeNode) *[]*TreeNode {
    s := make([]*TreeNode,0)
    var lastVisited *TreeNode
    for s != nil || root != nil {
        if root != nil {
            s = append(s,root)
            root = root.Left
        } else {
            node := s[len(s)-1]
            if node.Right != nil && lastVisited != node.Right {
                root = node.Right
            } else {
                if node == n {
                    return &s
                }
                lastVisited = s[len(s)-1]
                s = s[:len(s)-1]
                root = nil
            }
        }
        
    }
    return &s
}
```

\258. Add Digits

```go

class Solution:
    def addDigits(self, num: int) -> int:
        while num//10 > 0:
            temp = 0
            while(num > 0):
                temp += num % 10
                num //= 10
            num = temp
        return num

```

```go

func addDigits(num int) int {
    for num/10 > 0 {
        temp := 0
        for num > 0 {
            temp = temp + num %10
            num = num /10
        }
        num = temp
    
    }
    return num
}
```



\235**. Lowest Common Ancestor of a Binary Search Tree**

```go

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    
     min_ := min(q.Val,p.Val)
     max_ := max(q.Val,p.Val)
     if root == nil {
         return root
     }
     if root.Val <= max_ && root.Val >= min_ { //z在区间内,递归从root到叶子
         return root
     }
     if root.Val < min_ {
         return lowestCommonAncestor(root.Right, p, q)
     } else {
         return lowestCommonAncestor(root.Left, p, q)
     }
        
}



func min(a,b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}

func max(a,b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}
```

