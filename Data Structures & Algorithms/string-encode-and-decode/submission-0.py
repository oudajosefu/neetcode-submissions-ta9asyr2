class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{s}{chr(256)}'
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        temp = ''
        for char in s:
            if ord(char) == 256:
                res.append(temp)
                temp = ''
                continue
            temp += char
        return res
            
