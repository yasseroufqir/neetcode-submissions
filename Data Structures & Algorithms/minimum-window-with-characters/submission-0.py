class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Required character frequencies
        Ref = {}
        for char in t:
            Ref[char] = Ref.get(char, 0) + 1

        # Window character frequencies
        window = {}

        # Number of distinct character requirements not yet satisfied
        charNeeded = len(Ref)

        l = 0
        best_l = 0
        best_r = float("inf")

        for r in range(len(s)):

            # Add s[r] to the window
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # We have just satisfied one character requirement
            if char in Ref and window[char] == Ref[char]:
                charNeeded -= 1

            # Window is valid → try shrinking it
            while charNeeded == 0:

                # Update best answer
                if r - l < best_r - best_l:
                    best_l = l
                    best_r = r

                # Remove s[l]
                left_char = s[l]
                window[left_char] -= 1

                # We just broke a requirement
                if left_char in Ref and window[left_char] < Ref[left_char]:
                    charNeeded += 1

                l += 1

        if best_r == float("inf"):
            return ""

        return s[best_l:best_r + 1]