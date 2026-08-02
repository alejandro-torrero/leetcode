class Solution(object):
    def predictTheWinner(self, nums):
        return self.take(nums, 0, len(nums) - 1, 1, 0, 0)

    def take(self, nums, i, j, turn, p1, p2, lookup = None):
        lookup = {} if lookup is None else lookup
        
        if ()
        # print("p1: ", p1, " p2: ", p2)
        if i == j:
            # print("Final", i, j)
            # Last turn
            if turn == 1:
                # print(p1 + nums[i], p2)
                return (p1 + nums[i]) >= p2
            else:
                # print(p1, p2 + nums[i])
                return p1 >= (p2 + nums[i])

        if turn == 1:
            # p1 turn

            return self.take(nums, i + 1, j, 2, p1 + nums[i], p2) or self.take(
                nums, i, j - 1, 2, p1 + nums[j], p2
            )
        else:
            # p2 turn
            return self.take(nums, i + 1, j, 1, p1, p2 + nums[i]) or self.take(
                nums, i, j - 1, 1, p1, p2 + nums[j]
            )


sol = Solution()

print(sol.predictTheWinner([1, 5, 2]))
