class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for _ in range(len(nums)+1)]
        for num in nums:
            counter[num] = 1 + counter.get(num,0)
        for num, count in counter.items():
            freq[count].append(num)

        res = []
        for batch in reversed(freq):
            for num in batch:
                res.append(num)
                if (len(res)==k):
                    return res
        
        
        