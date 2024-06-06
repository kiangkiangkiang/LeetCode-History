from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_c = Counter(hand)
        hand_c = sorted([[k, v] for k, v in hand_c.items()], key=lambda x: x[0])
        # print(hand_c)

        while hand_c:
            last_num = None
            counter = 0
            pointer = 0
            while counter < groupSize:
                if not hand_c or pointer >= len(hand_c):
                    return False
                hand_c[pointer][1] -= 1
                this_num = hand_c[pointer][0]
                if last_num is not None:
                    if last_num + 1 != this_num:
                        return False

                last_num = this_num

                if hand_c[pointer][1] <= 0:
                    hand_c.pop(pointer)
                else:
                    pointer += 1
                counter += 1
        return True


aa = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3

aa = [1, 2, 3, 4, 5]
groupSize = 4

aa = [1, 1, 2, 2, 3, 3]
groupSize = 2

aa = [5, 1, 0, 6, 4, 5, 3, 0, 8, 9]
groupSize = 2
a = Solution()
print(a.isNStraightHand(aa, groupSize))
