class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a= len(nums)/2
        freq={}
        maj=0
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        for key, val in freq.items():
            if val >=a:
                maj= key
        return (maj)

        