class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}

        for x in s:
            h1[x] = h1.get(x, 0) + 1
        
        for y in t:
            if h1.get(y):
                h1[y] = h1.get(y) - 1
            else:
                return False
        
        for z in h1:
            if h1.get(z) != 0:
                return False
        

        return True
            
        