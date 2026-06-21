class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        for s in strs:
            placed = False
            for group in result:
                if self.isAnagram(group[0], s):
                    group.append(s)
                    placed = True
                    break
            if not placed:
                result.append([s])
        return result
    
    def isAnagram(self, left: str, right: str) -> bool:
       return sorted(left) == sorted(right)