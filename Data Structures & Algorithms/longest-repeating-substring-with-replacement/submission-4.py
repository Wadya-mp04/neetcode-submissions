class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        l,r=0,1
        longest = 1
        length = 1
        EMM = 0 #earliest mismatch
        counter = k
        while r<len(s):
            if (s[r] == s[l]):
                length+=1
                longest = max(longest,length)
            elif (s[r] != s[l]):
                if(counter==k ):
                    EMM = r
                    counter-=1
                    length+=1
                    longest = max(longest,length)
                    r+=1
                elif(counter>0):
                    counter-=1
                    length+=1
                    longest = max(longest,length)
                    r+=1
                else:
                    l=EMM
                    r=l+1
                    counter = k
                    length = 1
        
        return longest


        