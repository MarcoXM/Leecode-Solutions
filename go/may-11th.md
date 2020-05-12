## may-11th



```go

func firstUniqChar(s string) int {
    if len(s) == 0 {
        return -1
    
    }
    // 不需要key 为 string,这要快点
    var dit = make(map[rune]int) //构建dit values 为int 单个
    for _,v := range s {
        dit[v]++
    }
    for i,v := range s {
        if dit[v] == 1 {
            return i
        }
    }
    return -1
}
```



189. **Rotate Array**

```go
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k -= len(nums)
        nums[:] = nums[-k:]+nums[:-k]
## 有事觉得python slice 太方便了.
```

```go

func rotate(nums []int, k int)  {
    k =k%len(nums)
    if k == 0 {
        return 
    }
    var step, idx int
    temp := nums[0]
    for step < len(nums) {
        target_idx := (idx + k)%len(nums)
        // 分类讨论,取模后的idx 是否是同一个环 
        for target_idx != idx {
            temp , nums[target_idx] = nums[target_idx],temp
            target_idx = (target_idx + k)%len(nums)
            step ++ 
        } 
        idx ++
        temp , nums[target_idx] = nums[idx],temp
        step ++ 
        
    }
}
```



````go
//还是reverse 好写
func rotate(nums []int, k int)  {
    k =k%len(nums)
    if k == 0 {
        return 
    }
    reverse(nums,0,len(nums)-1)
    reverse(nums,0,k-1)
    reverse(nums,k,len(nums)-1)
}

func reverse(nums []int, l int, r int) {
    for l <= r {
        nums[l],nums[r] = nums[r],nums[l]
        l++
        r--
    }
}

````

