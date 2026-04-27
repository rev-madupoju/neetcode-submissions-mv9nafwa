class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """Brute-force"""
        for i in range(len(nums)):
            # skip the "i is j" with range of j starting at i + 1
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False