class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        if(len(s)<=1):
            return 1
        l,r = 0,0
        maxL = 1 
        counter = {}
        while r<len(s):
            counter[s[r]] = 1 + counter.get(s[r],0)
            if (counter[s[r]]>1):
                while s[l] != s[r]:
                    counter[s[l]] -=1
                    l+=1
                counter[s[l]] -=1
                l+=1
            length = r-l+1
            maxL = max(maxL,length)
            r+=1
        return maxL


            

