class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp [i] = dp[i + len (w) ]
                if dp[i]:
                    break
        return dp[0]
        # l = 0
        # i = 0
        # ls = []
        # while(i<len(s)):
        #     for j in range(i,len(s)):
        #         print(s[i:j+1])
        #         if s[i:j+1] in wordDict and s[i:j+2] not in wordDict: 
        #             ls.append(s[i:j+1])
        #             print(s[i:j+1])
        #             i = j
        #             break
        #     i+=1
        # print(ls)
        # for k in ls:
        #     if k not in wordDict:
        #         return False
        # return True






        