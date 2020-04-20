## april-19th

3. L**ongest Substring Without Repeating Characters**

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## 还是数据结构,一眼看过去就是 queue了 
        ## 区分sub string sub seq 而且只返回长度不用打印出来
        from collections import deque,defaultdict
        q = deque()
        dit = defaultdict(int)
        ans = 0
        for i in range(len(s)):
            if dit.get(s[i]) == None:
                q.append(i)
                dit[s[i]] = i
                ans = max(ans,len(q))

            elif dit.get(s[i])!= None:

                while s[q[0]]!=s[i]:
                    del dit[s[q[0]]]
                    q.popleft()
                q.popleft()
                dit[s[i]] = i
                q.append(i)
                
        return ans # O(N)
    
    ## 优化,不需要queue
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## 还是数据结构,一眼看过去就是 queue了 
        ## 区分sub string sub seq 而且只返回长度不用打印出来
        from collections import deque,defaultdict
        dit = defaultdict(int)
        ans = 0
        left = -1
        for i in range(len(s)):
            if dit.get(s[i])!= None and dit[s[i]] > left:
                left = dit[s[i]]
            dit[s[i]] = i
            ans = max(ans,i - left)     
        return ans
```

