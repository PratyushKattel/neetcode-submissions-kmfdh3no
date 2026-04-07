from collections import Counter,defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        chars = set(s)
        max_len = 0
        for char in chars:
            left = 0 
            count = 0
            for right in range (length):
                if s[right] == char :
                    count += 1
                while (right - left +1 ) - (count ) >k:
                    if s[left] == char :
                        count -= 1
                    left += 1

                max_len = max (max_len, right - left + 1)
        return max_len        

