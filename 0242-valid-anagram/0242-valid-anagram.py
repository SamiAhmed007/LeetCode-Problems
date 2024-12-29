class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(s)!= len(t):
            return False
        dic = {i:0 for i in range(26)}

        for i in range(len(s)):
            dic[ord(s[i]) - ord('a')] += 1
            dic[ord(t[i]) - ord('a')] -= 1
        for i in dic.values():
            if i!=0:
                return False
        return True
