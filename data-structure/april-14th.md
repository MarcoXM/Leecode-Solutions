# april-14th

1. **Design Twitter**

```python
class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict,deque
        self.database = defaultdict(list) ## user_id :
        self.followship = defaultdict(set)
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.timestamp += 1
        self.database[userId].append((-self.timestamp,tweetId)) ## 放入database 应该为tuple等type 元素


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        users = self.followship.get(userId)
        if users == None:
            users = []
        else:
            users = list(users)
        users = users + [userId]
        posts = [self.database[u][:] for u in users if self.database.get(u)!=None]
        h = [list(t[-1])+[i] for i,t in enumerate(posts)]
        heapq.heapify(h)
        res = []
        while h:
            if len(res) < 10:
                time,tweet,idx = heapq.heappop(h)
                res.append(tweet)
                posts[idx].pop()
                if posts[idx]:
                    heapq.heappush(h,list(posts[idx][-1]) +[idx])
            if len(res) >= 10:
                return res
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId: # 保证不能自己follow自己
            self.followship[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if self.followship.get(followerId) and (followeeId in self.followship[followerId]):
            self.followship[followerId].remove(followeeId)
        ### Python的变量内存关系真的要好学习,不想学习就应该建一个新的object.指针指向下一个变量的好处就是,变量不需要删减.
        ## OODesign ,还是建个class 好 bug free 很多问题直接可以避免


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```

