## april-25th

#### Searching

> **Completeness:** Is the algorithm guaranteed to find a solution when there is one?
> **Optimality:** Does the strategy find the optimal solution, as defined on page 68?
> **Time complexity:** How long does it take to find a solution?
> **Space complexity:** How much memory is needed to perform the search?
>
> 关键就是上面的标准,来衡量具体那个bfs更适用.
>
> 实际就是DFS可以递归, **代码少**,所以我用得多!
>

**搜索问题的本质就是图的遍历!! **

**让你在一幅「图」中找到从起点** **`start`** **到终点** **`target`** **的最近距离**

#### BFS

![bfs](../img/bfs.png)

1. 模板

   分析一下BFS就是齐头并进,非常适合找最短的结果,非常适合不需要**打印**结果的题目

```python
# 计算从起点 start 到终点 target 的最近距离
def bfs(start,target) {
    q = deque() # 核心数据结构
    visited = set() # 避免走回头路

    q.append(start); # 将起点加入队列
    visited.add(start);
    step = 0 # 记录扩散的步数

    while (q not empty):
        sz = len(q);
        # 将当前队列中的所有节点向四周扩散
        for i in range(sz):
            cur = q.leftpop()
            # 划重点：这里判断是否到达终点 
            if (cur is target):
                return step
            # 将 cur 的相邻节点加入队列
            for (next_x : cur.adj()):
                if (x not in visited):
                    q.append(x)
                    visited.add(x)
        # 划重点：更新步数在这里 
        step += 1 ##层数

```

BFS 可以找到最短距离，但是**空间复杂度高(看最后的表)，而 DFS 的**空间复杂度较低。但是据说大神都喜欢BFS

2. **BFS可以找到最短距离，DFS 不行吗**？

   BFS 的逻辑，`depth` 每增加一次，队列中的所有节点都向前迈一步，这保证了第一次到达终点的时候，走的步数是最少的。

   DFS 当然其实也是可以的，但是时间复杂度相对高很多。 BFS 借助队列做到一次一步「齐头并进」，是可以在**不遍历完整棵树的条件下找到最短距离**的, 都不用走完就找到结果了!!! DFS 实际上是靠递归的堆栈记录走过的路径，你要找到最短路径，肯定得把二叉树中所有树杈都探索完才能对比出最短的路径有多长对不对？。一个走完一个不走完,肯定BFS快. 而且空间确实比时间便宜.


#### DFS

![dfs](../img/dfs.png)

3. DFS解法-backtracking 

   1. 模板

   ```python
      result = []
      def backtrack(路径, 选择列表):
          if 满足结束条件:
              result.add(路径)
              return
      
          for 选择 in 选择列表:
              做选择
              backtrack(路径, 选择列表)
              撤销选择
   ```

      **其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」**

   2. 总结
   回溯算法就是个多叉树的遍历问题，关键就是在前序遍历和后序遍历的位置做一些操作

   2. **Surrounded Regions**

   ```python
   class Solution:
       def solve(self, board: List[List[str]]) -> None:
           """
           Do not return anything, modify board in-place instead.
           """
           ### DFS 好一点 空间要的更少
           if not board: return
   
           R = len(board)
           C = len(board[0])
           if R < 3 or C < 3: return
           
           def dfs(i,j):
               board[i][j] = "#"
               for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                   ni,nj = i+x,j+y
                   if 0 < ni <  R and  0 < nj < C  and board[ni][nj] == 'O':
                       dfs(ni,nj)
           # 运行
           for j in range(C):
               if board[0][j] =="O":
                   dfs(0, j)
               if board[R-1][j] =="O":
                   dfs(R - 1, j)
   
           for i in range(R):
               if board[i][0] =="O":
                   dfs(i, 0)
               if board[i][C-1] =="O":
                   dfs(i, C - 1)
           
           for i in range(0, R):
               for j in range(0,C):
                   if board[i][j] == 'O':
                       board[i][j] = 'X'
                   if board[i][j] == '#':
                       board[i][j] = 'O'
   
   ```
   
4. Back-tracking 变体

   其实就是减了更多的枝,其实BFS本质上都是暴力解法,只是更聪明的减少不需要暴力的地方.减少需要遍历的点. 我们的树就剪了枝丫zhiya

   ```python
   def backtrack(...):
       for 选择 in 选择列表:
           做选择
           backtrack(...)
           撤销选择
   ```

5. 使用情况

![table_bd](../img/table_bd.png)

图表来至 AI 3