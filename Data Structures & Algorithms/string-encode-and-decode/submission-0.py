class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        left = 0
        
        while(left < len(s)):
            right = left

            while s[right] != '#':
                right += 1
            
            length = int(s[left:right])
            start = right + 1
            end = start + length

            decoded_list.append(s[start:end])
            left = end

        return decoded_list
            