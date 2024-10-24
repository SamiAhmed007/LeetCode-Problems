class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)<3:
            return list(set(nums))
        nums.sort()
        cnt = 1
        res = []
        for i in range(0,len(nums)-1):
            if nums[i+1] == nums[i]:
                cnt+=1
                if cnt> len(nums)/3:
                    res.append(nums[i])
            else:
                cnt = 1
            
        return list(set(res))
        
        