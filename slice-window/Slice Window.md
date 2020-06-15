### Slice Window



Sliding Window 总结：
When: 在一个长string/list里面找符合条件的substring/sublistHow: 双指针标记一个window来代表当前的子字符串，滑动这个window并在过程中检验是否符合题目要求要求的时间复杂度往往是O(n)，空间复杂度往往是常数级的。根据 [leetcode 这个 tag summary](https://leetcode.com/tag/sliding-window/)，sliding window 比较少见easy题目，但不是sliding window本身有多难，基本都是难在变量的维护、指针移动条件的判断等细节，题目变化比较多，sliding window 本身的写法都是类似的。

​	三种题目类型：

窗口大小不变：

Find All Anagrams in a String[ https://leetcode.com/problems/find-all-anagrams-in-a-string/](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        r = l = 0
        needs = { k : p.count(k) for k in p}
        windows = collections.defaultdict(int)
        match = 0
        ans = []
        while r < len(s):
            w = s[r]
            if w in needs:
                windows[w] += 1
                if windows[w] == needs[w]:
                    match += 1    
            r += 1
            while match == len(needs):
                if r - l == len(p):
                    ans.append(l)
                w2 = s[l]
                if w2 in needs:
                    windows[w2] -= 1
                    if windows[w2] < needs[w2]:
                        match -= 1  
                l += 1
                    
        return ans
```



Permutation in String[ https://leetcode.com/problems/permutation-in-string/](https://leetcode.com/problems/permutation-in-string/)

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windows = collections.defaultdict(int)
        needs = {k:s1.count(k) for k in s1}
        l, r = 0,0
        match = 0
        while r < len(s2):
            w = s2[r]
            if w in needs:
                windows[w] += 1
                if windows[w] == needs[w]:
                    match += 1
            r += 1
            while match == len(needs):
                if r - l == len(s1):
                    return True
                w2 = s2[l]
                if w2 in needs:
                    windows[w2] -= 1
                    if windows[w2] < needs[w2]:
                        match -= 1
                        
                l += 1
        return False
    ## On 額外空間(26)
     
```





1100. Find K-Length Substrings With No Repeated Characters[ ](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/)（这题 lintcode 好像没有，但题挺好的，是我看到窗口大小不变的唯一难点的题，所以我就贴blog上了...）
      https://xuqiangwen1994.gitbook.io/practice/sliding-window/1100.-find-k-length-substrings-with-no-repeated-characters



窗口大小可变：

Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## 还是数据结构,一眼看过去就是 queue了 
        ## 区分sub string sub seq 而且只返回长度不用打印出来
        ans = 0
        r, l = 0, 0 
        windows = collections.defaultdict(int)
        while r < len(s):
            w = s[r]
            if w not in windows or windows[w] == 0 :
                ans = max(ans,r - l+1)        
            windows[w] += 1 
            r += 1
            while windows[w] == 2:
                w2 = s[l]
                windows[w2] -= 1
                l += 1
                
        return ans
        
```

Minimum Window Substring[ https://leetcode.com/problems/minimum-window-substring/](https://leetcode.com/problems/minimum-window-substring/)

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs = {k : t.count(k) for k in t}
        windows = collections.defaultdict(int)
        r,l = 0,0
        ans = 0
        min_length = 2 << 31 - 1
        match = 0
        while r < len(s):
            w = s[r]
            if w in needs:
                windows[w] += 1
                if windows[w] == needs[w]:
                    match += 1
            r += 1
            
            while match == len(needs):
                if r - l < min_length:
                    min_length = r - l
                    ans = l
                    
                w2 = s[l]
                if w2 in needs:
                    windows[w2] -= 1
                    if windows[w2] < needs[w2]:
                        match -= 1
                l += 1
        return s[ans:ans+min_length] if min_length != 2 << 31 - 1 else ""
```



Longest Substring with At Most Two Distinct Characters[ ](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)https://www.lintcode.com/problem/longest-substring-with-at-most-two-distinct-characters/description

```python
class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # Write your code here
        windows = collections.defaultdict(int)
        r,l = 0,0
        ans = 0
        
        while r< len(s):
            w = s[r]
            windows[w] += 1
            r += 1
            
            while len(windows) > 2:
                w2 = s[l]
                windows[w2] -= 1
                if windows[w2] == 0:
                    del windows[w2]
                l += 1
                
            ans = max(r-l,ans)
        return ans
                
```



Longest Substring with At Most K Distinct Characters （跟159基本是同一道题）[ ](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters/note/207548424. 

```python
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        windows = collections.defaultdict(int)
        r, l = 0, 0 
        length = 0
        while r < len(s):
            w = s[r]
            windows[w] += 1
            r += 1
            while len(windows) > k:
                w2 = s[l]
                windows[w2] -= 1
                if windows[w2] == 0:
                    del windows[w2]
                l += 1
                                
            length = max(length,r - l)
        return length
```



Longest Repeating Character Replacement[ https://leetcode.com/problems/longest-repeating-character-replacement/](https://leetcode.com/problems/longest-repeating-character-replacement/)

````go
func characterReplacement(s string, k int) int {
    windows := make([]int,26)
    var l, r, ans, maxCount int
    for r < len(s) {
        windows[s[r] - 'A'] ++
        maxCount = max(maxCount,windows[s[r] - 'A'])
        r++
        
        for r - l - maxCount > k{
            windows[s[l] - 'A'] --
            l ++
        }
        ans = max(ans,r - l)
        
    }
    return ans
}


func max (a int, b int) int {
    if a > b {
        return a
    }
    return b
}
````





Subarrays with K Different Integers[ https://leetcode.com/problems/subarrays-with-k-different-integers/](https://leetcode.com/problems/subarrays-with-k-different-integers/)

```python
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ##
        ans = l1 = l2 = r = 0
        windows1 = collections.defaultdict(int)
        windows2 = collections.defaultdict(int)
        while r < len(A):
            n = A[r]
            windows1[n] += 1
            windows2[n] += 1
            r += 1
            while len(windows1) > K:
                n2 = A[l1]
                windows1[n2] -= 1
                if windows1[n2] == 0:
                    del windows1[n2]
                l1 += 1
            while len(windows2) >= K:
                n2 = A[l2]
                windows2[n2] -= 1
                if windows2[n2] == 0:
                    del windows2[n2]
                l2 += 1
                
            ans += l2 - l1
        return ans
```



特殊数据结构：



Sliding Window Maximum[ https://leetcode.com/problems/sliding-window-maximum/](https://leetcode.com/problems/sliding-window-maximum/)

```go
func maxSlidingWindow(nums []int, k int) []int {
    q := make([]int,0)
    ans := make([]int,0)
    for r:=0; r < len(nums); r++ {
        //区间双闭
        if len(q) > 0 && q[0] <= r - k{
            q = q[1:] //保持size 
        }
        
        for len(q) > 0 && nums[r] > nums[q[len(q)-1]]{
            q = q[:len(q)-1]
        }
        q = append(q,r)
        
        if r - k >= -1{
            ans = append(ans,nums[q[0]]) 
        }

    }
    return ans
}
```



