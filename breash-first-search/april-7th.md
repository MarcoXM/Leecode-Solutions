# april 7th

200. **Number of Islands**

```python
## BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        from collections import deque
        q = deque()
        N = len(grid)
        M = len(grid[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        ans = 0
        ## 一个岛
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1":
                    ans +=1 ## 找到一个岛了
                    grid[i][j] = "0"
                    q.append((i,j))
                    while q:
                        x, y = q.pop()
                        for dx,dy in dirs:
                            nx,ny = x+dx, y+dy
                            if 0<=nx<N and 0<=ny<M and grid[nx][ny] == "1":
                                q.append((nx,ny))
                                grid[nx][ny]="0"
                                
        return ans
```

```go
type queue struct {
	row int
	col int
}
func numIslands(grid [][]byte) int {
    if len(grid) == 0 || len(grid[0]) == 0 {
        return 0
    }
    var N int = len(grid) 
    var M int = len(grid[0]) 
    var ans int
    var q []queue
    var dirs = []struct {
        x int
        y int
    }{
		{0, 1},
		{0,-1},
		{1, 0},
		{-1,0},
	}
    for i :=0 ;i < N; i++ {
        for j := 0 ; j < M; j++ {
            // fmt.Println(grid[i][j])
            if grid[i][j] != '1' {
                continue  
            }
            ans += 1
            q = append(q, queue{i, j})
            for len(q) > 0 { //for condition 就是 while
                node := q[0]
                x := node.row
                y := node.col
                q = q[1:] // 更新queue 
                for _,v := range dirs{
                    nx := x + v.x
                    ny := y + v.y
                    // fmt.Println(nx,ny)
                    if 0 <= nx && nx< N && 0<=ny && ny< M && grid[nx][ny]=='1' {
                        q = append(q,queue{nx,ny})
                        grid[nx][ny] = '0'
                    }             
                }
            }
        }
    }
    return ans
}

//还挺麻烦的
```



207. **Course Schedule**

```Python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        ## 
        
        if not prerequisites:
            return True
        from collections import deque,defaultdict
        course = defaultdict(list)
        indegree = defaultdict(int)
        for cour,pres in prerequisites:
            course[pres].append(cour)
            indegree[cour] += 1
            
        ## 如果形成环
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0: ## No prerequites
                q.append(i)
                
        ## 开始学习 能学的
        while q:
            node = q.popleft()
            for next_course in course[node]:
                indegree[next_course] -= 1 # 更新 预修list
                if indegree[next_course] == 0 :
                    q.append(next_course)
        return sum(indegree.values()) == 0
```

```go
type queue struct {
    course int
}

func canFinish(numCourses int, prerequisites [][]int) bool {
    if len(prerequisites) == 0{
        return true
    }
    var q []queue
    var courses = make(map[int][]int)
    var indegree = make([]int, numCourses) // 长度为多少们课
    
    for _,v := range prerequisites {
        indegree[v[0]]++ 
        courses[v[1]] = append(courses[v[1]],v[0])
    }

    for i := 0; i < numCourses; i++{
        if indegree[i] == 0{
            q = append(q,queue{i})
        }
    }
    for len(q)!=0 {
        node := q[0]
        q = q[1:]
        for _,v := range courses[node.course]{
            indegree[v]--
            if indegree[v] == 0 {
                q = append(q,queue{v})
            }
        }
    }
    for i := 0; i < numCourses; i++ {
		if indegree[i]!= 0 {
			return false
		}
	}
    return true
}
```



210. **Course Schedule II**
```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
             return list(range(numCourses))
        from collections import deque,defaultdict
        course = defaultdict(list)
        indegree = defaultdict(int)
        ans = []
        for cour,pres in prerequisites:
            course[pres].append(cour)
            indegree[cour] += 1
            
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            ans.append(node)
            for next_course in course[node]:
                indegree[next_course] -= 1 # 更新 预修list
                if indegree[next_course] == 0 :
                    q.append(next_course)
        return ans if len(ans)== numCourses else [] # 没学完就是没用
    
    
```

```go
type queue struct {
    course int
}
func findOrder(numCourses int, prerequisites [][]int) []int {
    var ans = make([]int,0) // 空list
    
    if len(prerequisites)==0{
        for i:=0;i< numCourses;i++ {
            ans = append(ans,i)
        }
        return ans
    }
    fmt.Println(ans)
    var q []queue
    var indegree = make([]int, numCourses) 
    var courses = make(map[int][]int)
    
    for _,v := range prerequisites {
        indegree[v[0]]++ 
        courses[v[1]] = append(courses[v[1]],v[0])
    }

    for i := 0; i < numCourses; i++{
        if indegree[i] == 0{
            q = append(q,queue{i})
        }
    }
    for len(q)!=0 {
        node := q[0]
        ans = append(ans,node.course)
        q = q[1:]
        for _,v := range courses[node.course]{
            indegree[v]--
            if indegree[v] == 0 {
                q = append(q,queue{v})
            }
        }
    }

    if len(ans) == numCourses{
        return ans
    } else {
        return make([]int, 0)
    }
}
    

```



127. **Word Ladder**

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        from collections import deque
        import string
        dirs = string.ascii_lowercase
        q = deque()
        ans = 0
        wordList = set(wordList)
        q.append((beginWord,1)) #
        while q:
            node,l = q.popleft()
            if node == endWord:
                return l
            for i in range(len(node)):
                for d in dirs: # 方向有26个
                    w = node[:i] + d + node[i+1:]
                    if w in wordList and w!=node:
                        wordList.remove(w)
                        q.append((w,l+1))    
        return 0
        
```

```go
type queue struct {
    word string
    length int
}

func ladderLength(beginWord string, endWord string, wordList []string) int {    
    var q []queue
    var words = make(map[string]struct{})
    var visited = make(map[string]struct{})
    for _, v := range wordList{
        words[v] = struct{}{}
    }
    if _, v := words[endWord]; !v {
        return 0
    }
    q = append(q,queue{beginWord,1})
    visited[beginWord] = struct{}{}
    for len(q)>0 {
        node := q[0]
        q = q[1:]
        if node.word == endWord{
            return node.length
        }
        for i:=0 ;i < len(node.word);i++{
            for j:= 'a'; j <= 'z'; j++ {
                //fmt.Println(j)
                w := node.word[:i] + string(j) + node.word[i+1:]
                _,vi := visited[w]
                if _,v := words[w]; v && w!=node.word && !vi{
                    q = append(q,queue{w,node.length + 1})
                    visited[w] = struct{}{}
                }
            }
        }
    }
    return 0
    
    
}   
```

605. **Sequence Reconstruction**

```python
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        if not org:
            return len(seqs) == 0
        ## 通过遍历seqs
        from collections import defaultdict,deque
        graphs = defaultdict(list)
        for sq in seqs:
            for i in range(len(sq)-1):
                graphs[sq[i]].append(sq[i+1])
                
        ## 剩下的就是能不能从node[0] 到 node[-1],能通且唯一
        ans = [[] for _ in range(len(org))]
        q = deque()
        q.append((org[0],0))
        while q:
            node,index = q.popleft()
            print(node)
            ans[index].append(node)
            next_nodes = graphs.get(node)
            if not next_nodes:
                continue
            for next_node in next_nodes:
                q.append((next_node,index+1))
                
        ans = list(map(lambda x : len(x)==1,ans))
        return len(ans) == len(seqs)
    ## 不写go 了 
        

```



133. **Clone Graph**

````python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        ## 上限100

        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return 
        from collections import deque
        q = deque()
        visited = dict() # node都有邻居 不需担心空value
        q.append(node)
        node_copy = Node(node.val, [])
        visited[node] = node_copy
        while q:
            node = q.popleft()
            if not node:
                continue
            for neightbor in node.neighbors:
                if neightbor not in visited:
                    visited[neightbor] = Node(neightbor.val, [])
                    q.append(neightbor)
                visited[node].neighbors.append(visited[neightbor])
        return node_copy

````

