class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def recur(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # Both strings exhausted
            if i == len(s1) and j == len(s2):
                return True

            # Try taking the next character from s1
            if i < len(s1) and s1[i] == s3[i + j]:
                if recur(i + 1, j):
                    memo[(i, j)] = True
                    return True

            # Try taking the next character from s2
            if j < len(s2) and s2[j] == s3[i + j]:
                if recur(i, j + 1):
                    memo[(i, j)] = True
                    return True

            memo[(i, j)] = False
            return False

        return recur(0, 0)