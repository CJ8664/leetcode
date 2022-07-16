class Twitter:

    def __init__(self):
        self.following_map = defaultdict(set) # follower -> followee
        self.tweets_map = defaultdict(lambda: deque(maxlen=10)) # user -> stack of tweet id
        self.ts = 0
          
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_map[userId].append((self.ts, tweetId))
        self.ts += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        uids = set()
        uids.add(userId)
        for uid in self.following_map[userId]:
            uids.add(uid)
        tweet_ids = []
        heapq.heapify(tweet_ids)
        n_idx = 1
        while len(tweet_ids) <= 10 and uids:
            uids_to_remove = set()
            for uid in uids:
                if len(self.tweets_map[uid]) >= n_idx:
                    heapq.heappush(tweet_ids, self.tweets_map[uid][-n_idx])
                else:
                    uids_to_remove.add(uid)
            uids = uids - uids_to_remove
            n_idx += 1
            while len(tweet_ids) > 10:
                heapq.heappop(tweet_ids)
            
        result = deque()
        for _ in range(min(10, len(tweet_ids))):
            _ts, tweet_id = heapq.heappop(tweet_ids)
            result.appendleft(tweet_id)
        return result   
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)
        
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following_map[followerId]:
            return None
        self.following_map[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)