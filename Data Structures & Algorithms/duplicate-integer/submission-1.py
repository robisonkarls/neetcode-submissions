class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_map = {}

        for n in nums:
            if n in dup_map:
                return True
            else:
                dup_map[n] = 1

        return False