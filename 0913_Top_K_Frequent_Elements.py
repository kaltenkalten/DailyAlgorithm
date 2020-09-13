class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from queue import PriorityQueue
        from collections import Counter
        
        d = Counter(nums)
        q = PriorityQueue()
        
        for key, value in d.items():
            q.put((value, key))
            if q.qsize() > k:
                q.get()
            
        result = []
        for i in range(k):
            #print("A")
            _, key = q.get()
            result.append(key)
            
        return result
