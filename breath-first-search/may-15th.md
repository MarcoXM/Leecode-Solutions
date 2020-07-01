# may-15th

```python
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ## 思路就是 遇到识别符,改变状态 根据状态加到ans
        ## 到时spilt用\n
        source = "\n".join(source) + "\n"
        ## 避免越界
        ans = ""
        i = 1
        n = len(source)
        stack = []
        while i < n:
            # print(stack)
            s = source[i-1] + source[i]
            if not stack and (s == "//" or s == "/*") :
                stack.append(s)
                i = i + 2
            elif s == "*/" and stack and stack[-1] =="/*":
                stack.pop()
                i = i + 2
            ## \n 长度为１　
            elif s[-1] == "\n" and stack and stack[-1] == "//":
                stack.pop()
                i += 1
            elif stack :
                i += 1
            else:
                ans += source[i-1] 
                i += 1
        ## filter 掉 \n\n\n
        return filter(len, ans.split('\n'))
```

```python
class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """
    def concatenetedString(self, s1, s2):
        # write your code here
        a =set(s1)
        b =set(s2)

        ab = a.intersection(b)
        ans = ''
        for i in s1+s2 :
            if i not in ab:
                ans += i

        return ans
    ## set
```

