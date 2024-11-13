class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp = 0
        ans = ""

        def check(s):
            if s[::] == s[::-1]:
                return True
            return False

        for i in range(len(s)):
            for j in range(i,len(s)+1):
                if check(s[i:j]):
                    # print(s[i:j],temp)
                    if len(s[i:j]) > temp:
                        ans = s[i:j]
                    temp = max(temp, len(s[i:j]))

        return ans
        