from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        prev = -1
        while bank:
            current_str = bank.pop(0)
            sum = len(current_str.replace("0", ""))
            if prev != -1:
                total = total + prev * sum
            prev = sum if sum != 0 else prev
        return total


bank = ["011001", "000000", "010100", "001000"]
a = Solution()
print(a.numberOfBeams(bank))
