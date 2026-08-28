class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maxVol = 0
        indices = ()
        while l<r:
            height = min(heights[l],heights[r])
            width = r-l
            vol = height * width
            if (vol>maxVol):
                maxVol = vol
                indices = (l,r)
            elif(heights[r]>heights[l]):
                l+=1
            else:
                r-=1
        return maxVol