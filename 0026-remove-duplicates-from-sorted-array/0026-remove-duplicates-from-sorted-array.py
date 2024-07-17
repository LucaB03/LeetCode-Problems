class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = None
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] == current:
                nums.remove(nums[i])
                l -= 1
            else: 
                current = nums[i]
                i += 1
        return len(nums)
