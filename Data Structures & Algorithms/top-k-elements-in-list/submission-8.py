from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        frequency = Counter(nums)
        
        bucket = [[] for _ in range(len(nums)+1)]
        for num, count in frequency.items():
            bucket[count].append(num)
        
        result = []
        for i in range(len(bucket) - 1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if(len(result) == k):
                    return result


























        # frequency = Counter(nums)

        # # buckets[i] contains numbers appearing i times
        # buckets = [[] for _ in range(len(nums) + 1)]

        # for number, count in frequency.items():
        #     buckets[count].append(number)

        # result = []

        # # Start with the highest frequency
        # for count in range(len(nums), 0, -1):
        #     for number in buckets[count]:
        #         result.append(number)

        #         if len(result) == k:
        #             return result