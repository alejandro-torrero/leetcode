class Solution(object):
    def stoneGame(self, piles):
        return self.take(piles, 0, len(piles) - 1, 1, 0, 0)

    def take(self, nums, i, j, turn, p1, p2, lookup=None):
        lookup = {} if lookup is None else lookup

        if (i, j, turn) in lookup:
            return lookup[(i, j, turn)]

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
            lookup[(i, j, turn)] = self.take(
                nums, i + 1, j, 2, p1 + nums[i], p2, lookup
            ) or self.take(nums, i, j - 1, 2, p1 + nums[j], p2, lookup)
            return lookup[(i, j, turn)]
        else:
            # p2 turn
            lookup[(i, j, turn)] = self.take(
                nums, i + 1, j, 1, p1, p2 + nums[i], lookup
            ) or self.take(nums, i, j - 1, 1, p1, p2 + nums[j], lookup)
            return lookup[(i, j, turn)]


sol = Solution()

print(sol.stoneGame([5, 3, 4, 5]))
