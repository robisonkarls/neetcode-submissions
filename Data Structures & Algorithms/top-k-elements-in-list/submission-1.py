class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            buckets[value].append(key)
        
        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for n in buckets[count]:
                result.append(n)
                if len(result) == k:
                    return result
        return result