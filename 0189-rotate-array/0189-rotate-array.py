class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        l = nums[len(nums)-k:len(nums)+1]+nums[:len(nums)-k]
        # print(l)
        for i in range(len(l)):
            nums[i] = l[i]


        