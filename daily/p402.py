class Solution:
    def find_min(self, num, current_pointer, last_choice):
        min_num = 10000000
        min_pointer = -1
        while current_pointer <= last_choice:

            if int(num[current_pointer]) < min_num:
                min_num = int(num[current_pointer])
                min_pointer = current_pointer

            current_pointer += 1
        return str(min_num), min_pointer

    def removeKdigits(self, num: str, k: int) -> str:
        total_digits = len(num) - k
        current_pointer = 0
        last_choice = len(num) - total_digits
        num = list(num)
        result = []
        while len(result) <= total_digits and last_choice < len(num):
            min_num, min_pointer = self.find_min(num, current_pointer, last_choice)
            result.append(min_num)
            current_pointer = min_pointer + 1

            last_choice += 1
            # print(result)

        final_result = ""
        for i in range(len(result)):
            if result[i] != "0":
                final_result = "".join(result[i:])
                break
        return final_result if final_result else "0"


num = "1432219"
k = 3
num = "10200"
k = 1  # expect 200
a = Solution()
print(a.removeKdigits(num, k))
