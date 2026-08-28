class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            s = "#" + str(len(s)) + "#" + s
            encoded+=s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            prefix = s[:3]
            s = s[3:]
            # print(s)
            # print(prefix)
            key = int(prefix[1])
            word = s[:key]
            # print("word:" + word)
            res.append(word)
            s = s[key:]
            print(s)
        return res



