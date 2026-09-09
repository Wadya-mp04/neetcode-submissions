class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        pivotIndex = 0
        while l<r:
            mid = (l+r)//2
            if (nums[mid]>nums[-1]):
                l = mid + 1
            else:
                r = mid 

        pivotIndex = l
                
        print(pivotIndex)
        l, r = 0, len(nums) - 1

        if target >= nums[pivotIndex] and target <= nums[r]:
            l = pivotIndex
        else:
            r = pivotIndex - 1

        while l<=r:
            mid = (l+r)//2
            if (nums[mid] == target):
                return mid
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid + 1
        return -1 

        