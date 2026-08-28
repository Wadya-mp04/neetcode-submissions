class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count final frequencies
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
            
        # 2. Map frequencies to buckets (size needs to be len(nums) + 1)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            bucket[freq].append(num)
            
        # 3. Collect the top k frequent elements from right to left
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

