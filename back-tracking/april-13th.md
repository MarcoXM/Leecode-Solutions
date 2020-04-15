## april-13th



126. **Word Ladder II**

```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        ## 首先这就是搜索了 找到就是最短的,并打印了 
        ## DFS,回溯也是可以的 
        ## 默写模板
        
        import string 
        from collections import defaultdict
        dirs = string.ascii_lowercase
        ans = defaultdict(list)
        if endWord not in wordList:
            return []
        
        tmp = [beginWord]
        if beginWord in wordList:
            wordList.pop(wordList.index(beginWord))
        N = len(wordList)
        visited = [-1] * N
        def bt(dis,tmp):
            ### 终止条件
            if tmp[-1] == endWord:
                ans[dis].append(tmp)
                
            for i in range(N):
                if visited[i] == 1:
                    continue
                if self.isValid(tmp[-1],wordList[i]):
                    visited[i] = 1
                    bt(dis+1,tmp + [wordList[i]])
                    visited[i] = -1
        bt(0,tmp)
        return [] if not ans.keys() else ans[min(ans.keys())]
                        
    def isValid(self,w1,w2):
        return sum(list(map(lambda x : x[0]==x[1],zip(w1,w2))))== len(w1)-1
            
        ## 超时,DFS还是不行 主要是不知道最短距离
        ## 层次遍历
        
        
        
        
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        ## 首先这就是搜索了 找到就是最短的,并打印了 
        from collections import deque
        import string
        dirs = string.ascii_lowercase
        q = deque() 
        ans = []
        level = 1
        minLevel = 9999
        wordList.append(beginWord)
        wordList = set(wordList)
        q.append([beginWord])
        visited = set(beginWord)
        while len(q)>0:
            nodes = q.popleft()
            # print(q)
            if level < len(nodes):
                level = len(nodes)
                if level > minLevel:
                    break  
            node = nodes[-1]
            for i in range(len(beginWord)):
                for d in dirs:
                    w = node[:i] + d + node[i+1:]
                    if w in wordList and w!=node and w not in nodes:
                        new_nodes = nodes[:] + [w]
                        if w == endWord:
                            ans.append(new_nodes)
                            minLevel = level
                        else:
                            q.append(new_nodes)
                        # wordList.remove(w)
        return ans
    ## BFS 一层一层挖,记录底层数,超时
   	## bfs 再剪枝 !! 用更多空间换时间
    
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        ## 首先这就是搜索了 找到就是最短的,并打印了 
        if endWord not in wordList:
            return []
        from collections import defaultdict
        import string
        dirs = string.ascii_lowercase
    
        wordList = set(wordList) # 
        layer = {}
        layer[beginWord] = [[beginWord]] 

        while layer:
            newlayer = defaultdict(list) # hash [word] :[seq,seq]
            for word in layer:
                if word == endWord: 
                    return layer[word] 
                for i in range(len(word)): # 遍历每一个可能性
                    for c in dirs:
                        w =  word[:i] + c + word[i+1:]
                        if w in wordList:
                            newlayer[w] += [j + [w] for j in layer[word]] # old_seq + w
            wordList -= set(newlayer.keys()) # remove from dictionary to prevent loops
            layer = newlayer # move down to new layer

        return []
        
        
```



829. **Word Pattern II**

```python
class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, s):
        # write your code here
        if len(pattern) < 1 :
            return False 
        elif len(pattern) ==1:
            return True
            
        ## 还是理解为树的遍历,层数为len(pattern)
        ## 生成一个字典,走一步,用hashtable 记录对应走的 string,
        ## 下次走的是时候先查询,看最后能否走完 string
        
        from collections import defaultdict
        dit = {} ## p-char  s 
        visited = set()
        return self.helper(pattern,s,0,0,dit,visited)
        
    def helper(self,pattern,s, p, idx, dit, visited):
        if (p == len(pattern) and idx == len(s)):
            return True
        if (p == len(pattern) or idx == len(s)):
            return False

        pattern_char = pattern[p] 
        for i in range(idx,len(s)):
            sub = s[idx:i+1]
            if dit.get(pattern_char) == sub:
                if self.helper(pattern, s, p + 1, i + 1 , dit, visited):
                    return True
            
            elif dit.get(pattern_char) == None:
                if sub in visited:
                    continue
                
                dit[pattern_char] = sub
                visited.add(sub)
                # print(dit,visited,len(visited))
                if self.helper(pattern,s, p + 1, i + 1, dit, visited):
                    return True
                visited.remove(sub)
                del dit[pattern_char]
                
        return False

```

