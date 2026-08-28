class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for letter in s:
            if letter in hash:
                hash[letter] = hash[letter]+1
            else:
                hash[letter] = 1
        for letter in t:
            if letter not in hash:
                return False
            if hash.get(letter) == 0:
                return False
            
            hash[letter] = hash[letter] - 1

        for value in hash.values():
            if value != 0:
                return False

        return True

        