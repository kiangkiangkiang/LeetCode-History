from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        result = 0

        def helper(heights: List[int], bricks: int, ladders: int, result):
            for i in range(len(heights) - 1):
                remain = heights[i + 1] - heights[i]
                if remain > 0:
                    if bricks >= remain and ladders > 0:
                        # Case 1
                        case1_result = helper(heights[i + 1 :], bricks - remain, ladders, result + 1)

                        # Case 2
                        case2_result = helper(heights[i + 1 :], bricks, ladders - 1, result + 1)

                        return case1_result if case1_result > case2_result else case2_result
                    elif bricks >= remain and ladders <= 0:
                        bricks -= remain
                    elif bricks < remain and ladders > 0:
                        ladders -= 1
                    else:
                        break
                result += 1
            return result

        return helper(heights, bricks, ladders, result)


import heapq


class Solution:
    def heappush_max(self, heap, item):
        heap.append(item)
        heapq._siftdown_max(heap, 0, len(heap) - 1)

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        result = 0
        accu = 0
        accu_list = []
        for i in range(len(heights) - 1):
            remain = heights[i + 1] - heights[i]
            if remain > 0:
                accu += remain
                self.heappush_max(accu_list, remain)
                if accu > bricks:
                    if ladders > 0:
                        while ladders > 0 and accu > bricks:
                            max_num = heapq._heappop_max(accu_list)
                            accu -= max_num
                            ladders -= 1
                        if accu > bricks:
                            break
                    else:
                        break
            result += 1
        return result


heights = [4, 2, 7, 6, 9, 14, 12]
bricks = 5
ladders = 1


# heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
# bricks = 10
# ladders = 2

heights = [14, 3, 19, 3]
bricks = 17
ladders = 0


heights = [1, 5, 1, 2, 3, 4, 10000]
bricks = 4
ladders = 1
a = Solution()
print(a.furthestBuilding(heights, bricks, ladders))
