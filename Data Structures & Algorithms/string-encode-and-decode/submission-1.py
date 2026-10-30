class Solution:
    cache = [0] * 26

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "/" + s

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        pointer = 0
        
        while pointer < len(s):
            length = ""
            string = ""

            while s[pointer] != "/":
                length += s[pointer]
                pointer += 1
            
            length = int(length)

            start = pointer + 1
            end = start + length
            string = s[start:end]

            res.append(string)
            pointer += length + 1
        
        return res


            



