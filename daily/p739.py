import heapq
from typing import List

# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days
# you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]


class Solution:
    def heappush_max(self, heap, item):
        heap.append(item)
        heapq._siftdown_max(heap, 0, len(heap) - 1)

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        current_temperature = temperatures.pop(0)
        diff_list = []
        locate_list = []
        index = 0
        while temperatures:
            next_temperature = temperatures.pop(0)
            diff = next_temperature - current_temperature
            if diff_list:
                # remove_item = []
                n = len(diff_list)
                for i in range(n):
                    diff_list[i] += diff
                    if diff_list[i] > 0:

                for i in reversed(range(n)):
                    diff_list[i] += diff
                    if diff_list[i] > 0:
                        # remove_item.append(i)
                        result[locate_list[i]] = index - locate_list[i] + 1
                        diff_list.pop(i)
                        locate_list.pop(i)

            if diff > 0:
                result[index] = 1
            else:
                self.heappush_max(diff_list, (diff, index))
                # self.heappush_max(locate_list, index)
                # diff_list.append(diff)
                # locate_list.append(index)
            index += 1
            current_temperature = next_temperature

        return result


# input = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
input = [73, 74, 75, 71, 69, 72, 76, 73]
a = Solution()

print(a.dailyTemperatures(input))
