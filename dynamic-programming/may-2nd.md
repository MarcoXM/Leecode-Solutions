## may-2nd




````python

class Solution:
    def isValid(self, s: str) -> bool:
        if not s :return True
        d = {
            "(":")",
            "[":"]",
            "{":"}",
        }
        
        stack = [s[0]]
        
        for i in range(1,len(s)):
            if stack and s[i] == d.get(stack[-1]):
                stack.pop()
            else:
                stack.append(s[i])
            
        return len(stack) == 0
````



53. **Maximum Subarray**

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        ## 排除conern case 以后
        ans = cur = nums[0]
        
        for i in range(1,len(nums)):
            cur = max(nums[i],cur + nums[i]) ## 要不从新数起,要不一直累计 
            ans = max(ans,cur)
        return ans
```

```go

func maxSubArray(nums []int) int {
    if len(nums)==0 {
        return 0
    } else if len(nums) == 1 {
        return nums[0]
    }else {
        var ans int
        var cur int
        ans = nums[0]
        cur = nums[0]
        for i:=1; i < len(nums); i++ {
            cur = max(nums[i], nums[i] + cur)
            ans = max(ans,cur)
        }
        return ans 
    }
    
}

func max(a int,b int)int {
    if a > b {
        return a
    } else {
        return b
    }
}
```



```python
class Solution:
    def numDecodings(self, s: str) -> int:
        ### 这不是dp吗,打下来以后发现其实可以回溯好像
        ### 每次走两步 如果是1,或者2 
        self.ans = 0
        if not s:
            return 0

        self.dfs(s,0)
        return self.ans
    
    ### 重要的是分类讨论,得出结果.
    
    def dfs(self,s,idx):
        if idx == len(s):
            self.ans += 1
            return 
        
        if s[idx] == "0":
            return 
        
        if idx < len(s) - 1:
            if int(s[idx]+s[idx + 1])<= 26:
                self.dfs(s,idx + 2)

        self.dfs(s,idx + 1)
        
        ## 超时......
    
```



```go
func numDecodings(s string) int {
	return f(s,0)
}

func f(s string,idx int) int {
	if len(s) == idx {
		return 1
	}
	if s[idx] == '0' {
		return 0
	}

    
    ans1 := f(s,idx + 1)
    var ans2 int
    if idx < len(s)-1 && (s[idx]-'0')*10+s[idx + 1]-'0' <= 26 {
		ans2 = f(s, idx + 2)
	}
	return ans1 + ans2
}
//换 go 可以了 700ms
```



```python
class Solution:
    def numDecodings(self, s: str) -> int:
        ### 这不是dp吗,打下来以后发现其实可以回溯好像
        ### 每次走两步 如果是1,或者2 
        if not s :
            return 0
        
        dp = [0] * (len(s)+1) # null + len(s) 状态
        dp[-1] = 1 ## 必有解
        if s[-1] != "0":
            dp[-2] = 1
        
        ## 反向遍历会因为新来的信息,更改过去的结果
        for i in range(len(s)-2,-1,-1):
            if s[i] == "0":
                continue
            if int(s[i]+s[i + 1]) <= 26:
                dp[i] += dp[i+2]
                
            dp[i] += dp[i+1] ## 从call function 到 查表
        return dp[0]
    # DP
```

