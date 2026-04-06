from collections import Counter,defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        max_len = 0
        for i in range (length):
            sub_str=s[i]
            for j in range (i + 1 ,length ):
                sub_str += s[j]
                frequency_substr=Counter(sub_str)
                rep_num = (j - i + 1) - frequency_substr.most_common()[0][1]
                if rep_num <= k:
                    max_len = max((j-i + 1),max_len)
        return max_len
                
                
        

