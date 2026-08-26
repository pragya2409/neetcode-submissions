class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt=0
        low=0
        high=len(nums)-1
        while low<=high:
            if nums[low]!= val:
                low += 1
            elif nums[high]== val:
                cnt += 1
                high -= 1
            else:
                cnt +=1
                nums[low],nums[high]=nums[high],nums[low]
                low += 1
                high-=1
        k=len(nums)-cnt
        return(k)
                





