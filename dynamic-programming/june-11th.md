# june-11th

[https://leetcode.com/problems/top-k-frequent-words/](https://leetcode.com/problems/top-k-frequent-words/)

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # O(n log k) time and O(n) extra space. 
        # 不加限制做法
        # 后面查了,为啥heap这个做法klogn...
        word_count = collections.defaultdict(int)
        for w in words:
            word_count[w]+=1

        candidates = [(-word_count[w],w) for w in word_count.keys()]
        heapq.heapify(candidates)
        ans = []
        while len(ans) <k:
            _,element = heapq.heappop(candidates)
            ans.append(element)

        return ans
```

\1730. Spreadsheet Notation Conversion

```python
class Solution:
    """
    @param index: the index to be converted
    @return: return the string after convert.
    """
    def convert(self, index):
        # write your code here702


        ## 深深理解了 0 base的好处
        ans = ""
        d = (index-1)//702
        l = (index-1)%702
        ans = ans + str(d+1)
        print(l)
        if l <26:
            ans = ans + chr(l+64+1)
            return  ans

        else:
            s = l%26 + 1
            l = l//26
            ans = ans + chr(l+64)
            ans = ans + chr(s+64)

            return ans
```

\1293. Shortest Path in a Grid with Obstacles Elimination

```python
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ## 最短路
        ## 周赛考这个难度就好了
        if len(grid)==1 and len(grid[0])==1 : return  0

        if k - (len(grid) + len(grid[0]) - 3) >= 0:
            return len(grid) + len(grid[0]) - 2

        q = collections.deque()
        visited = set()
        step = 0
        q.append((0,0,k))

        while q:
            step += 1
            ls = len(q)
            for _ in range(ls):
                x,y,k = q.popleft()
                if k < 0 :
                    continue
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    newx,newy = x+dx , y + dy
                    ## 越界
                    if self.isObs(newx,newy,grid) is None:
                        continue
                    ## 是否找到
                    if newx == len(grid)-1 and newy == len(grid[0])-1:
                        return step
                    ## 是障碍
                    if not self.isObs(newx,newy,grid):
                        new_k = k
                    elif self.isObs(newx,newy,grid):
                        new_k = k - 1

                    if (newx,newy,new_k) in visited:
                        continue
                    q.append((newx,newy,new_k))
                    visited.add((newx,newy,new_k))

        return -1

    def isObs(self,x,y,grid):
        if 0 <=x< len(grid) and 0<=y<len(grid[0]):
            if grid[x][y] == 1:
                return True
            else:
                return False
        else:
            return
```

