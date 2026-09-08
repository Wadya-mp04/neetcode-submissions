import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        # print(r)
        time = 0;
        minR = 0
        while l<=r:
            valid = True
            mid = (l + r) // 2
            # print(mid)
            for p in piles:
                time += math.ceil(p/mid)
                if time > h:
                    time = 0
                    l = mid + 1
                    valid = False
                    break
            if valid:
                minR = mid
                r = mid -1
                time = 0
        return minR

            

