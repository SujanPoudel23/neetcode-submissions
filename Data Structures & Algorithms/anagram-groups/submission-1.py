class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        result = []

        for s in strs:
            build = [0] * 26
            for c in s:
                build[ord(c) - ord('a')] += 1
            
            tup = tuple(build)
            if tup in cache:
                index = cache[tup]
                result[index].append(s)
            else:
                cache[tup] = len(result)
                result.append([s])

        return result