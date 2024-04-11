import heapq


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        total_digits = len(num) - k
        last_choice = len(num) - total_digits

        candidate_pool = []
        for i, value in enumerate(num[:last_choice]):
            heapq.heappush(candidate_pool, (int(value), i))

        current_pointer = 0
        result = []
        while last_choice < len(num):
            while candidate_pool and candidate_pool[0][1] < current_pointer:
                heapq.heappop(candidate_pool)

            if int(num[last_choice]) < candidate_pool[0][0]:
                result.extend(num[last_choice:])
                break
            else:
                if candidate_pool:
                    result.append(str(candidate_pool[0][0]))
                    current_pointer = candidate_pool[0][1] + 1
                    heapq.heappop(candidate_pool)
                    heapq.heappush(candidate_pool, (int(num[last_choice]), last_choice))
                    last_choice += 1
                else:
                    result.extend(num[last_choice:])
                    break

        final_result = ""
        for i in range(len(result)):
            if result[i] != "0":
                final_result = "".join(result[i:])
                break
        return final_result if final_result else "0"


num = "1432219"
k = 3
# num = "10200"
# k = 1  # expect 200
# num = "43214321"
# k = 4  # expect "1321"
a = Solution()
print(a.removeKdigits(num, k))
