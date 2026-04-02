class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}#{s}'
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        s_len = ''
        i = 0
        while i < len(s):
            char = s[i]
            s_len += char
            if char == '#':
                num = int(s_len[:-1])
                res.append(s[i+1:i+1+num])
                s_len = ''
                i = i + 1 + num
            else:
                i += 1
        return res
            
