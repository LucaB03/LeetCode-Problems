class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        try:
            index = nums.index(val)
        except ValueError:
            return len(nums)
        while index < len(nums) and nums[index] == val:
            nums.pop(index)
        return len(nums)
            