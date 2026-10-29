class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_cache = {}

        for n in nums:
            if n in freq_cache:
                freq_cache[n] += 1
            else:
                freq_cache[n] = 1
        
        freq_table = []
        for number, frequency in freq_cache.items():
            freq_table.append((frequency, number))

        heapq.heapify_max(freq_table)
        result = []
        for i in range(k):
            result.append(heapq.heappop_max(freq_table)[1])
        
        return result