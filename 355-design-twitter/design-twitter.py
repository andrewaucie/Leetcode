class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.following = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.posts[userId].append((self.timestamp, tweetId))
        if len(self.posts[userId]) > 10:
            self.posts[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        # loop through following, insert 10 most recent in each into a maxheap of size 10, return maxheap
        mostRecent = []
        # Add following user's posts
        for followeeId in self.following[userId]:
            for timestamp, tweetId in self.posts[followeeId]:
                heapq.heappush(mostRecent, (-timestamp, tweetId))
        
        # Add own user's posts
        for timestamp, tweetId in self.posts[userId]:
            heapq.heappush(mostRecent, (-timestamp, tweetId))
        
        res = []
        for _ in range(min(10, len(mostRecent))):
            res.append(heapq.heappop(mostRecent)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)