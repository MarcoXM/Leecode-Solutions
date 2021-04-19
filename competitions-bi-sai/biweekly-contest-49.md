# biweekly-contest-49

1812. determine-color-of-a-chessboard-square

```python
## 暴力，模拟
class Solution:
    def squareIsWhite(self, c: str) -> bool:
        w = c[0]
        row = int(c[1]) 
        col = ord(w) - ord("a") + 1
        
        if row %2 == 0 :
            if col%2== 0 :
                return False
            else:
                return True
            
        else:
            if col%2== 0 :
                return True
            else:
                return False
        
```



1813. sentence-similarity-iii

> 一个句子是由一些单词与它们之间的单个空格组成，且句子的开头和结尾没有多余空格。比方说，"Hello World" ，"HELLO" ，"hello world hello world" 都是句子。每个单词都 只 包含大写和小写英文字母。
>
> 如果两个句子 sentence1 和 sentence2 ，可以通过往其中一个句子插入一个任意的句子（可以是空句子）而得到另一个句子，那么我们称这两个句子是 相似的 。比方说，sentence1 = "Hello my name is Jane" 且 sentence2 = "Hello Jane" ，我们可以往 sentence2 中 "Hello" 和 "Jane" 之间插入 "my name is" 得到 sentence1 。
>
> 给你两个句子 sentence1 和 sentence2 ，如果 sentence1 和 sentence2 是相似的，请你返回 true ，否则返回 false 。

```python
## 再保存第一眼居然看不懂。。 字符串用python

class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if len(s1) <= len(s2):
            s1 , s2 = s2 , s1
        s1 = s1.split()
        s2 = s2.split()
        ## s1 longer
        ans = 0
        left = -1
        for i in range(len(s1)):
            if i < len(s2) and s1[i] == s2[i]:
                # print(s1[i], s2[i],s1,s2)
                ans += 1
            else:
                left = i
                break
            
        for j in range(len(s1) - 1, left, -1):
            if j - (len(s1) - len(s2)) >= 0 and s1[j] == s2[j - (len(s1) - len(s2))]:
                # print(s1[j], s2[j - (len(s1) - len(s2))], s1, s2)
                ans += 1
        return ans >= len(s2)
```



1814. count-nice-pairs-in-an-array

> 给你一个数组 nums ，数组中只包含非负整数。定义 rev\(x\) 的值为将整数 x 各个数字位反转得到的结果。比方说 rev\(123\) = 321 ， rev\(120\) = 21 。我们称满足下面条件的下标对 \(i, j\) 是 好的 ：
>
> 0 &lt;= i &lt; j &lt; nums.length nums\[i\] + rev\(nums\[j\]\) == nums\[j\] + rev\(nums\[i\]\) 请你返回好下标对的数目。由于结果可能会很大，请将结果对 109 + 7 取余 后返回。

```python

## 哈希 组合数学 ，记得取模就好了 
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        
        def flip(n):
            t = 0
            while n:
                t = t * 10 + (n % 10)
                n //= 10
            return t
        
        
        # rev = collections.defaultdict(int)
        cnt = collections.defaultdict(int)
        for n in nums:
            tmp = flip(n)
            # rev[n] = tmp

            cnt[(n - tmp)] += 1
        # print(cnt)
        ans = 0
        for k, v in cnt.items():
            # print(k, v)
            ans += (v * (v - 1) // 2 )% mod
                
                
        return ans
            
```



1815. maximum-number-of-groups-getting-fresh-donuts

> 有一个甜甜圈商店，每批次都烤 batchSize 个甜甜圈。这个店铺有个规则，就是在烤一批新的甜甜圈时，之前 所有 甜甜圈都必须已经全部销售完毕。给你一个整数 batchSize 和一个整数数组 groups ，数组中的每个整数都代表一批前来购买甜甜圈的顾客，其中 groups\[i\] 表示这一批顾客的人数。每一位顾客都恰好只要一个甜甜圈。
>
> 当有一批顾客来到商店时，他们所有人都必须在下一批顾客来之前购买完甜甜圈。如果一批顾客中第一位顾客得到的甜甜圈不是上一组剩下的，那么这一组人都会很开心。
>
> 你可以随意安排每批顾客到来的顺序。请你返回在此前提下，最多 有多少组人会感到开心

```python

## 模拟退火 epoch = 70 
t=start 1e6, end 1e-5, 衰退率 0.97

## 这题的考点就是这个。 通过设立全局变量找到最优值，需要调参
class Solution:
    def maxHappyGroups(self, b: int, groups: List[int]) -> int:
        import random 
        import numpy as np
        if b == 1:return len(groups)
        
        groups = [x% b for x in groups]
        
        self.ans = 1
        def check():
            pre = 0
            ans = 0
            for i in range(len(groups)):
                if pre == 0 :
                    ans += 1
                pre = (pre + groups[i]) % b
            self.ans = max(self.ans, ans) 
            return ans
        
        
        def simmulate_anneal():
            random.shuffle(groups)
            t = 1e6
            while t > 1e-5 :
                a = random.randint(0, len(groups) - 1)
                b = random.randint(0, len(groups) - 1)
                if a == b:continue
                x = check()
                groups[a], groups[b] = groups[b],groups[a]
                y = check()
                delta = y - x  ## 变小了。。假设
                if delta < 0 and  np.exp(delta/t) > random.random():
                    groups[a], groups[b] = groups[b],groups[a]
                t *=0.97
                
        for i in range(70):
            simmulate_anneal()
        return self.ans
```

