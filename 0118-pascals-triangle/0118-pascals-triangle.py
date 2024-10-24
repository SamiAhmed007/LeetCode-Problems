class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        res = []
        ans = [1]
        res.append(ans)
        cnt = 1
        while(cnt<numRows):
            ans_len = len(ans)
            l = []
            l.append(ans[0])
            for indx in range(ans_len-1):
                l.append(ans[indx]+ans[indx+1])
            l.append(ans[-1])
            cnt+=1
            ans_len = len(l)
            ans = l
            res.append(l)
        return res
            


        