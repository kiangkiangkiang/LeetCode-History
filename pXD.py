from typing import List


def haha(input_list: List[str]) -> List[List[str]]:
    def combination(s: str, s_list: List[List[str]]):
        result = []
        for possible_ans in s_list:
            result.extend([possible_ans[:i] + [s] + possible_ans[i:] for i in range(len(possible_ans) + 1)])
        return result

    prev_ans = []
    for s in input_list:
        if not prev_ans:
            prev_ans = [[s]]
        else:
            prev_ans = combination(s, prev_ans)
    return prev_ans


print(haha(["1", "2", "3", "4"]))
