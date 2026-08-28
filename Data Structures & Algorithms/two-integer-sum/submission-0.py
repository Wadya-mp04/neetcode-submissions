class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}    
        for i,num in enumerate(nums):
            if num in table:
                return [table.get(num),i]
            complement = target - num
            table[complement] = i

