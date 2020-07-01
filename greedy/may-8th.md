# may-8nd

1. **Copy List with Random Pointer**

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
        return head
    }
    // 申请内存地址
    q, newHead := head, &Node{}
    p := newHead
    d := make(map[*Node]*Node) //这个是node to node 的map

    for q != nil {
        // 是否有记录
        if d[q] == nil {
            d[q] = &Node{Val: q.Val}
        }
        // cppy 当前节点
        p.Next = d[q]
        p = p.Next

        // Ramdon 是否指向nil
        if q.Random == nil {
            d[q].Random = nil
        }else {
            // 判断 Random 在不在map
            if d[q.Random] == nil {
                d[q.Random] = &Node{Val: q.Random.Val}
            }
            // 记录map
            p.Random = d[q.Random]
        }
        q = q.Next
    }
    return newHead.Next
}
```

1. Integer to English Words

```go
import "strings"

var bigMap = map[int]string{
    1: "Thousand",
    2: "Million",
    3: "Billion",
}

var digitStr = map[int]string{
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
}

var twentyStr = map[int]string{
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
}

var teenStr = map[int]string{
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
}

func numberToWords(num int) (rtn string) {
    var digit int
    for num > 0 {
        if num%1000 != 0 {
            rtn = numberToWords3WithDigit(num%1000, digit) + " " + rtn
        }
        num /= 1000
        digit++
    }
    if rtn == "" {
        return digitStr[0]
    }
    return strings.TrimSpace(rtn)
}

func numberToWords3WithDigit(num int, digit int) string {
    if digit > 0 {
        return numberToWords3(num) + " " + bigMap[digit]
    } else {
        return numberToWords3(num)
    }
}

func numberToWords3(num int) string {
    if num < 10 {
        return digitStr[num]
    } else if num < 20 {
        return twentyStr[num]
    } else if num < 100 {
        if num%10 == 0 {
            return teenStr[num/10]
        } else {
            return teenStr[num/10] + " " + digitStr[num%10]
        }
    } else {
        if num%100 == 0 {
            return digitStr[num/100] + " " + "Hundred"
        } else {
            return digitStr[num/100] + " " + "Hundred " + numberToWords3(num%100)
        }
    }
}
```

1. Remove Duplicates from Sorted Array

```go
func removeDuplicates(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    var curr int
    for i,_ := range nums {
        if nums[i] != nums[curr] {
            curr ++
            nums[i],nums[curr] = nums[curr],nums[i]
        }
    }
    return curr + 1
}
```

1. Reverse Words in a String

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        return " ".join(s.split()[::-1])
```

1. Sort Colors

```go
func sortColors(nums []int)  {
    // 只有三个值
    if len(nums) == 0  {
        return
    }

    var l,i int 
    r := len(nums)-1
    // 双闭区间, 终止条件 大于
    for i <= r {
        if nums[i] == 0 {
            nums[l],nums[i] = nums[i],nums[l]
            i ++
            l ++
        } else if nums[i] == 1 {
            i++
        } else if  nums[i] == 2 {

            nums[r],nums[i] = nums[i],nums[r]
            r --
        }
    }
}
```

1. Matrix finding number

```go
func findingNumber(m [][]int) int {
    d = make(map[int]int)
    for i := 0 ; i < len(m); i++ {
        for j :=0 ; j < len(m[0]); j++ {
            d[m[i][j]] ++
        }
    }
    ans := -1 
    for k,v := range d {
        if v == len(m) {
            ans  = k
        } 
    }
    return k
}
```

\134. Gas Station

```go
// 好像考点都是贪心,那就做了1
func canCompleteCircuit(gas []int, cost []int) int {
    var start_idx,ttgas,gain int
    for i:= 0; i<len(gas);i++ {
        ttgas = gas[i] - cost[i] + ttgas
        gain = gas[i] - cost[i] + gain
        //增加不够,当前这一代人失败了,从一个继续计数,欠着的还有tt记着
        if gain < 0 {
            start_idx = i + 1
            gain = 0 
        } 
    }
    //账本tt 还记着欠多少
    if ttgas < 0 {
        return -1
    } else {
        return start_idx
    }

}
```

