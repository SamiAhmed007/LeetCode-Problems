class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        ans = 0
        for elem in res:
            if elem-1 not in res:
                length = 1
                cnt = 1
                while elem+length in res:
                    length += 1
                    cnt += 1
                ans = max(ans, cnt)
        return ans