from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # order = set(order)
        # dict_order = {v: k for k, v in enumerate(order)}

        dict_order = {v: k for k, v in enumerate(reversed(order))}
        stat_s = Counter(s)
        new_s = {k: [-1, -1] for k in stat_s}
        for k in new_s:
            new_s[k][0] = stat_s[k]
            if k in dict_order:
                new_s[k][1] = dict_order[k]

        new_s = sorted(new_s.items(), key=lambda x: x[1][1], reverse=True)
        result = ""
        for item in new_s:
            result = result + item[0] * item[1][0]
        return result


order = "kqep"
s = "pekeq"
"kqep"
exp = "kqeep"
a = Solution()
print(a.customSortString(order, s))
