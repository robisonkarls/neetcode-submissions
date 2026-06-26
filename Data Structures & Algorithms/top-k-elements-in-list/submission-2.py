class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, counter in freq.items():
            bucket[counter].append(num)
        
        result = []
        for count in range(len(bucket) - 1, 0, -1):
            for num in bucket[count]:
                result.append(num)
                if len(result) == k:
                    return result
        return result