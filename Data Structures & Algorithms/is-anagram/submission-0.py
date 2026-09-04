class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_for_string1 = [0] * 26
        count_for_string2 = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            count_for_string1[ord(s[i]) - ord('a')] += 1
            count_for_string2[ord(t[i]) - ord('a')] += 1
        
        if count_for_string1 == count_for_string2:
            return True
        else:
            return False
