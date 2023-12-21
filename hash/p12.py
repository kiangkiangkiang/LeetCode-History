"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class test:
    trans_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    trans_list = list(trans_dict.keys())

    def intToRoman(self, num: int) -> str:
        m_list = str(num)[:-3]
        num_list = list(str(num)[-3:][::-1])
        result = int(m_list) * int(10 ** len(num_list) / 1000) * "M" if m_list else ""

        while num_list:
            num = int(num_list.pop())
            if num != 0:
                unit = 10 ** len(num_list)
                unit = 1 if unit == 0 else unit
                if num == 4 or num == 9:
                    result += self.trans_dict[unit]
                    result += self.trans_dict[(num + 1) * unit]
                elif num == 5 or num == 1:
                    result += self.trans_dict[num * unit]
                else:
                    this_num = unit * num
                    index = len(self.trans_list) - 1
                    while this_num > 0:
                        if this_num >= self.trans_list[index]:
                            this_num -= self.trans_list[index]
                            result += self.trans_dict[self.trans_list[index]]
                            index = len(self.trans_list) - 1
                        else:
                            index -= 1
        return result


test_i = 1994
# test_i = 58
test_i = 3
# test_i = 14
a = test()
result = a.intToRoman(test_i)
print(result)
# Done
