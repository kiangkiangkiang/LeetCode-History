class Solution:
    def intToRoman(self, num: int) -> str:
        # convert_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # convert_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        # convert_dict = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        convert_int = [1000, 500, 100, 50, 10, 5, 1]
        convert_roman = ["M", "D", "C", "L", "X", "V", "I"]
        convert_indicators = 0
        total = len(convert_int)
        result = ""

        while convert_indicators < total:
            if num >= convert_int[convert_indicators]:
                num -= convert_int[convert_indicators]
                result += convert_roman[convert_indicators]
            else:
                convert_indicators += 1
        # 處理 4, 9, 14, 19, 24, 29, 34, ...
        return result


num = 29
ans = Solution()
result = ans.intToRoman(num=num)
print(result)
