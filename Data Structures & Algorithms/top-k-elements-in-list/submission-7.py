from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        frequency = Counter(nums)

        # buckets[i] contains numbers appearing i times
        buckets = [[] for _ in range(len(nums) + 1)]

        for number, count in frequency.items():
            buckets[count].append(number)

        result = []

        # Start with the highest frequency
        for count in range(len(nums), 0, -1):
            for number in buckets[count]:
                result.append(number)

                if len(result) == k:
                    return result