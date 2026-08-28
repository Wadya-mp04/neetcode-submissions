class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        if(len(s)<=1):
            return 1
        l,r = 0,0
        maxL = 1 
        lastSeen = {}
        while r<len(s):
            if (s[r] in lastSeen and lastSeen[s[r]]>=l):
                l = lastSeen[s[r]] + 1
                lastSeen[s[r]] = r
            lastSeen[s[r]] = r
            maxL = max(maxL,r-l+1)
            r+=1
        return maxL


            

