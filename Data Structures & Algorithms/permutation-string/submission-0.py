class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0,0
        letters = {}
        for char in s1:
            letters[char] = 1 + letters.get(char,0)
        counter = letters.copy()
        while r<len(s2):
            if s2[r] in counter:
                counter[s2[r]] -=1
                if counter[s2[r]]<0:
                    while counter[s2[r]]<0:
                        counter[s2[l]]+=1
                        l+=1
                if counter[s2[r]] == 0:
                    valid = True
                    for value in counter.values():
                        if value != 0:
                            valid = False
                            break
                    if valid:
                        return True
                r+=1
            else:
                r+=1
                l=r
                counter = letters.copy()
                continue
        return False