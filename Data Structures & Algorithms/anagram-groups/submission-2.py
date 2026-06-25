class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        for i, word in enumerate(strs):
            placed = False
            for group in result:
                if sorted(word) == sorted(group[0]):
                    group.append(word)
                    placed = True
            if not placed:
                result.append([word])
        return result
                    