class Solution(object):
    def distFn(self, w1, w2, i=0, j=0, lookup=None):
        lookup = {} if lookup is None else lookup
        n = len(w1)
        m = len(w2)

        if (i, j) in lookup:
            return lookup[(i, j)]

        if i == n:
            lookup[(i, j)] = m - j
            return lookup[(i, j)]

        if j == m:
            lookup[(i, j)] = n - i
            return lookup[(i, j)]

        if w1[i] == w2[j]:
            lookup[(i, j)] = self.distFn(w1, w2, i + 1, j + 1, lookup)
            return lookup[(i, j)]

        lookup[(i, j)] = 1 + min(
            self.distFn(w1, w2, i + 1, j, lookup),
            self.distFn(w1, w2, i, j + 1, lookup),
            self.distFn(w1, w2, i + 1, j + 1, lookup),
        )

        return lookup[(i, j)]
    
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.distFn(word1,word2)


