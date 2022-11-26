class Solution:
    def search(self, nums, target: int) -> int:
        r = len(nums)-1
        l = 0
        if r == -1:
            return -1
        while True:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[l + (r-l)//2] < target:
                l += (r-l)//2
            elif nums[l + (r-l)//2] > target:
                r -= (r-l)//2
            elif nums[l + (r-l)//2] == target:
                return l + (r-l)//2
            if (r-l)//2 == 0:
                break
        return -1

sol = Solution()
print(sol.search([-1, 0, 2, 3, 4, 5] ,12))