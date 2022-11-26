class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        i = 0
        while i + k < len(nums)-1:
            if nums[i] == 0:
                k += 1
            else:
                i += 1
            nums[i] = nums[i+k]
        for i in range(1, k+1):
            nums[-i] = 0
        print(k, nums)

sol = Solution()
print(sol.moveZeroes([0, 1, 0, 2, 12]))