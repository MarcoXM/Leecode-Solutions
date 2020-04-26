## april-23th

\784. **Letter Case Permutation**

```python

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:        
        
        # 要打印结果
        path = ""
        def helper(idx,path):
            if idx >= len(S):
                ans.append(path)
                return
            if S[idx].isalpha():
                if ord(S[idx]) > ord("Z") :
                    helper(idx+1,path + chr(ord(S[idx]) - 32))
                else:
                    helper(idx+1,path + chr(ord(S[idx]) + 32))
            helper(idx+1,path + S[idx])                    
        ans = []
        helper(0,"")
        return ans
                    
                    
                
```

```go
func letterCasePermutation(S string) []string {
    ans := []string{}
	dfs([]byte(S), 0, &ans) // &指针告诉地址
	return ans
}

func dfs(s []byte, i int, ans *[]string) {
	if i == len(s) {
		*ans = append(*ans, string(s))
		return
	}

    // 直接加一,稍后修改
	dfs(s, i+1, ans)

	if isAlphabet(s[i]) {
		s[i] ^= (1 << 5) // 32
		dfs(s, i+1, ans)
	}
}
//自己定义
func isAlphabet(c byte) bool {
    if (c >= 65 && c <= 90) || (c >= 97 && c <= 122 ) {
		return true
	}
    return false
}
```



\171. **Excel Sheet Column Number**

```go

func titleToNumber(s string) int {
    var ans int
    for i:=0; i < len(s);i++ {
        ans = int(s[i] - 64)+ ans * 26
    }
    return ans
}   
```

