class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            encoded_string += f'{len(strs[i])}#{strs[i]}'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        left = 0
        decoded_string = []
        while(left < len(s)):
            right = left
            while(s[right] != "#"):
                right +=1
            length = int(s[left:right])
            start = right + 1
            end = start + length
            decoded_string.append(s[start:end])
            left = end
        return decoded_string