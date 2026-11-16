class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxL = height[l];
        maxR = height[r]; 
        wSum = 0
        while l<r:
            if (maxL<=maxR):
                l+=1
                if(l==r):
                    break
                wSum += max(0,maxL-height[l])
                if(height[l]>maxL):
                    maxL = height[l]
            else:
                r-=1
                if(l==r):
                    break
                wSum += max(0,maxR-height[r])
                if (height[r]>maxR):
                    maxR = height[r]
        return wSum