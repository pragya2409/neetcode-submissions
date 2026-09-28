class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            twosum= nums[l]+nums[r] 
            if twosum> target:
                r-=1
            elif twosum< target :
                l+=1
            else: 
                return [l+1, r+1]


        