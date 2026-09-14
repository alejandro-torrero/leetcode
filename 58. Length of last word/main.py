class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        print(f"-{s}-")
        splittedString = s.split(" ")

        return len(splittedString[-1])


sol = Solution()

print(sol.lengthOfLastWord("   fly me   to   the moon  "))