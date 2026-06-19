class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map[c] = 1
        
        s_len = len(s)

        for c in t:
            if c in s_map:
                s_map[c] -= 1
                c_occurrency = s_map[c]
                s_len -= 1
                if c_occurrency < 0:
                    return False
                if s_len < 0:
                    return False
            else:
                return False
        
        return True
