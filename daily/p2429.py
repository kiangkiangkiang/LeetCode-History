class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_str = bin(num2)[2:]
        num1_str = bin(num1)[2:]

        counter = 0
        for i in num2_str:
            if i == "1":
                counter += 1

        tmp = 0
        for i in num1_str:
            if i == "1":
                tmp += 1

        result = ["0"] * counter if counter > len(num1_str) else ["0"] * len(num1_str)
        pointer = 0
        while pointer < len(num1_str) and counter > 0:
            if num1_str[pointer] == "1":
                result[pointer] = "1"
                counter -= 1
            else:
                result[pointer] = "0"

            pointer += 1

        pointer = len(result) - 1
        while counter > 0 and pointer > 0:
            if result[pointer] == "0":
                result[pointer] = "1"

                counter -= 1
            pointer -= 1

        return int("".join(result), 2)


"""









.







.

"""

#
#
#
#
# 找到一個數是跟 num2 一樣多個 "1" 並且此數和 num1 做 XOR 會有最小值
num1 = 3
num2 = 5

num1 = 65
num2 = 84

num1 = 1
num2 = 12

num1 = 25
num2 = 72
a = Solution()
print(a.minimizeXor(num1, num2))
