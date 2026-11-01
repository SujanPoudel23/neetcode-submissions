class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        cache = set()
        l, r = 0, 0
        maxLength = 0

        while r < len(s):
            if s[r] not in cache:
                cache.add(s[r])
            else:
                while s[l] != s[r]:
                    cache.remove(s[l])
                    l += 1
                l += 1 # Get character one past the repeat 
            

            maxLength = max(maxLength, r - l + 1)
            r += 1
        
        return maxLength
            
