class Solution:
    def numSteps(self, s: str) -> int:
        counter = 0
        if s == "1":
            return 0
        s = list(s)
        while True:
            # print(s)
            zero_counter = 0
            if s[-1] == "1":  # odd
                pointer = len(s) - 1
                is_get_num = False
                while pointer >= 0:
                    if s[pointer] == "1":
                        s[pointer] = "0"
                        pointer -= 1
                    else:
                        s[pointer] = "1"
                        is_get_num = True
                        break
                counter += 1
                if not is_get_num:
                    s = ["1"] + s
            else:
                pointer = len(s) - 2
                while pointer >= 0:
                    if s[pointer] == "1":
                        s[pointer + 1] = "1"
                        s[pointer] = "0"
                        zero_counter += 1
                    pointer -= 1
                counter += 1
                if s[-1] == "1" and zero_counter == 1:
                    break

        return counter


s = "101"
a = Solution()
print(a.numSteps(s))
