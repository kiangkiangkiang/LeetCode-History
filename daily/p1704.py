class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        half = int(len(s) / 2)
        counter1, counter2 = 0, 0
        for i in s[:half]:
            if i in vowel:
                counter1 += 1

        for i in s[half:]:
            if i in vowel:
                counter2 += 1

        return True if counter1 == counter2 else False


s = "booolk"
a = Solution()
print(a.halvesAreAlike(s=s))
