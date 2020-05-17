## Slice Window



模板的python版本：

```python
def solution(s, t):
	# hash_记录t中字符出现的次数，window记录窗口中相应字符出现的次数
	hash_, window = {}, {}
	# 根据t构建hash_字典
	for c in t:
	    hash_[c] = hash_.get(c, 0) + 1
	# 初始化窗口左右边界，左闭右开区间 [left, right)
	left, right = 0, 0
	# valid表示窗口中满足要求的字符的个数
	valid = 0
	
	while right < len(s):
		# c是将移入窗口的字符
		c = s[right]
		# 窗口右移
		right += 1
		# 对窗口内数据进行更新
		...
		
		# 判断窗口是否需要收缩
		while (condition to shrink window):
			# d是将移除窗口的字符
			d = s[left]
			# 左移窗口
			left += 1
			# 窗口内数据更新
			...
```

滑动窗口算法的思路是这样：

1、我们在字符串 S 中使用双指针中的左右指针技巧，初始化 left = right = 0，把索引左闭右开区间 [left, right) 称为一个「窗口」。

2、我们先不断地增加 right 指针扩大窗口 [left, right)，直到窗口中的字符串符合要求（包含了 T 中的所有字符）。

3、此时，我们停止增加 right，转而不断增加 left 指针缩小窗口 [left, right)，直到窗口中的字符串不再符合要求（不包含 T 中的所有字符了）。同时，每次增加 left，我们都要更新一轮结果。

4、重复第 2 和第 3 步，直到 right 到达字符串 S 的尽头。

这个思路其实也不难，**第 2 步相当于在寻找一个「可行解」，然后第 3 步在优化这个「可行解」，最终找到最优解，**也就是最短的覆盖子串。左右指针轮流前进，窗口大小增增减减，窗口不断向右滑动，这就是「滑动窗口」这个名字的来历。



1、当移动 right 扩大窗口，即加入字符时，应该更新哪些数据？

2、什么条件下，窗口应该暂停扩大，开始移动 left 缩小窗口？

3、当移动 left 缩小窗口，即移出字符时，应该更新哪些数据？

4、我们要的结果应该在扩大窗口时还是缩小窗口时进行更新？




### 一、最小覆盖子串

LeetCode 76 题，Minimum Window Substring，难度 Hard：

```python

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        minLen = float('inf')
        left = 0  # 等右指针所在的位置之前的字符串包含t以后，左指针开始移动
        right = 0  # 右指针
        window = collections.defaultdict(int)
        needs = dict((i, t.count(i)) for i in t)
        match = 0
        
        ## 当右指针没越界
        while right < len(s):
            c1 = s[right]
            if c1 in needs.keys():
                window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1
            
            # 找到合适长度, 看看是不是要找的人 
            while match == len(needs):
                if right - left < minLen:
                    start = left
                    minLen = right - left
                c2 = s[left]
                if c2 in needs.keys():
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return '' if minLen == float('inf') else s[start:start + minLen]

```



### 二、字符串排列

LeetCode 567 题，Permutation in String，难度 Medium：

```python
class Solution:
    def checkInclusion(self, t: str, s: str) -> bool:
        start = 0
        left = 0  # 等右指针所在的位置之前的字符串包含t以后，左指针开始移动
        right = 0  # 右指针
        window = collections.defaultdict(int)
        needs = dict((i, t.count(i)) for i in t)
        match = 0
        
        ## 当右指针没越界
        while right < len(s):
            c1 = s[right]
            if c1 in needs.keys():
                window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1
            
            # 找到合适长度, 看看是不是要找的人 
            while match == len(needs):
                ## 关键判定,确定指针区间长度
                if right - left == len(t):
                    return True
                c2 = s[left]
                if c2 in needs.keys():
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return False

```





### 三、找所有字母异位词

这是 LeetCode 第 438 题，Find All Anagrams in a String，难度 Medium：

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        left = 0
        right = 0
        match = 0
        window = collections.defaultdict(int)
        needs = dict((i, p.count(i)) for i in p)

        while right < len(s):
            c1 = s[right]
            if c1 in needs.keys():
                window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            while match == len(needs):
                ## 判定加入res 
                if right - left == len(p):
                    res.append(left)
                c2 = s[left]
                if c2 in needs.keys():
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return res
```



### 四、最长无重复子串
这是 LeetCode 第 3 题，Longest Substring Without Repeating Characters，难度 Medium：

```python
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
    
    
     def lengthOfLongestSubstring(s):
         right = 0
         res = 0
         left = 0
         window = collections.defaultdict(int)

         while right < len(s):
             c1 = s[right]
             window[c1] += 1
             right += 1
             while window[c1] > 1:
                 c2 = s[left]
                 window[c2] -= 1
                 left += 1
             res = max(res, right-left)
         return res
```







