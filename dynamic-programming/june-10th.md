## june-10th

[
Back](https://www.lintcode.com/ladder/156/)1903. Department Statistics

```python
class Solution:
    """
    @param employees: information of the employees
    @param friendships: the friendships of employees
    @return: return the statistics
    """
    def departmentStatistics(self, employees, friendships):
        # write your code here.
        ## 有事感觉lintcode 的评级.. 这题一看就不像easy
        ## 再者这题特别像SQL
        ## 给一个fact table 和dimension table
        id_dep,dep_count = self.preprocess(employees)
        new_friends = self.job_friend(friendships,id_dep)

        ans = []
        for key in dep_count.keys():
            value = new_friends[key] if new_friends[key] else 0
            ans.append(f"{key}: {value} of {dep_count[key]}")
            
        return ans
        
    def preprocess(self,employees):
        dep_count = collections.defaultdict(int)
        id_dep = collections.defaultdict(int)
        
        for info in employees:
            id,name,department = info.split(",")
            dep_count[department.strip()] += 1
            id_dep[id] = department.strip()
        
        return id_dep,dep_count
        
    
    def job_friend(self,friendships,id_dep):
        visited = set()
        fri_dep = collections.defaultdict(int)
        
        for fp in friendships:
            x,y = fp.split(", ")
            if id_dep[x] != id_dep[y]:
                if x not in visited:
                    fri_dep[id_dep[x]]+=1
                    visited.add(x)
                if y not in visited:
                    fri_dep[id_dep[y]]+=1
                    visited.add(y)

        return fri_dep
    
                    
            
```

\1872. Minimum Cost to Connect Sticks

````python
class Solution:
    """
    @param sticks: the length of sticks
    @return: Minimum Cost to Connect Sticks
    """
    def MinimumCost(self, sticks):
        # write your code here
        import heapq
        heapq.heapify(sticks)
        
        ans = 0
        while len(sticks) > 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            ans += x+y
            heapq.heappush(sticks,x+y)
            
        return ans
        
````





```python
body = request.get_json()
feature1 = body.get('a')
feature2 = body.get('b')
feature3 = body.get('c')

```

