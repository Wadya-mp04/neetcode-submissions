class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            s = "#" + str(len(s)) + "#" + s
            encoded+=s
            # print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            i = 1
            while(s[i]!='#'):
                i+=1
            prefix = s[:i+1]
            s = s[i+1:]
            # print(s)
            # print(prefix)
            key = int(prefix[1:len(prefix)-1])
            word = s[:key]
            # print("word:" + word)
            res.append(word)
            s = s[key:]
            # print(s)
        return res



