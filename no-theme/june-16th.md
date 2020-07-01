# june-16th

\240. Search a 2D Matrix II

```go
func searchMatrix(matrix [][]int, target int) bool {
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return false
    }
    var row, left int
    if matrix[row][left] > target {
        return false
    }

    for row < len(matrix) {
        idx := biSearch(matrix[row],target,len(matrix[0]),left)
        if idx == len(matrix[0]) {
            row ++
        }else if matrix[row][idx] == target {
            return true
        }else if idx > 0 {
            row ++ 
        }else if matrix[row][idx] > target{
            return false
        }
    }
    return false
}


func biSearch( m []int, target , right , left int) int {
    // 有重复元素 没优化好
    for left < right {
        mid := (left + right)/2
        if m[mid] == target{
            return mid
        }else if m[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left

}
//NlogN
```

\138. Copy List with Random Pointer

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    if head == nil {
        return nil
    }
    q, dummy := head, &Node{} // dummy 是初始值的node
    p := dummy
    history := make(map[*Node]*Node)

    // 遍历 q 
    for q != nil {
        // 主要是一直更换q -> q = q.Next
        if history[q] == nil{
            history[q] = &Node{Val:q.Val}
        }
        // p 落后一个节点
        p.Next = history[q]
        // 弄完主干
        p = p.Next

        if q.Random != nil {
            if history[q.Random] == nil {
                history[q.Random] = &Node{Val : q.Random.Val}
            }
            p.Random = history[q.Random]
        }else {
            p.Random = nil
        }
        q = q.Next
    }
    return dummy.Next 

}
```

