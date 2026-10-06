class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        print("Sorted array", nums)
        for i in range(1,len(nums),2):
            print(nums[i],i)
            if nums[i-1] != nums[i]:
                return nums[i-1]

        return nums[-1]


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))