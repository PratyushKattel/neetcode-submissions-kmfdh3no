from collections import Counter,defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        max_len = 0
        for i in range (length):
            for j in range (i + 1 ,length + 1):
                sub_str = s[i:j]
                frequency_substr=Counter(sub_str)
                rep_num = (j-i) - frequency_substr.most_common()[0][1]
                if rep_num <= k:
                    max_len = max((j-i),max_len)
        return max_len
                
                
        

