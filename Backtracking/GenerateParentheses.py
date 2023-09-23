def generate_parentheses(n):
    max_len = 2 * n
    tail_total = n
    tail_current = [(0, 0)]
    result = []
    current_text = []
    two_way_pointer = []

    def drop_out_loop(current_text, two_way_pointer, tail_current):
        back_index = two_way_pointer.pop()
        # lask_symbol = current_text[back_index]
        current_text = current_text[:back_index] + [")"]
        tail_current = tail_current[: back_index + 1]
        tail_current.append((tail_current[back_index][0], tail_current[back_index][1] + 1))
        return current_text, two_way_pointer, tail_current

    while True:
        current_len = len(current_text)

        if current_len == max_len:
            result.append("".join(current_text))
            if not two_way_pointer:
                break
            current_text, two_way_pointer, tail_current = drop_out_loop(current_text, two_way_pointer, tail_current)
        else:
            tail_current.append((tail_current[current_len][0] + 1, tail_current[current_len][1]))
            two_way_pointer.append(current_len)
            current_text.append("(")

        if tail_current[-1][0] > tail_total or tail_current[-1][1] > tail_total or tail_current[1][1] == 1:
            if not two_way_pointer:
                break
            current_text, two_way_pointer, tail_current = drop_out_loop(current_text, two_way_pointer, tail_current)

        # print(current_text)
        # print(tail_current)
        # print(result)
        # print(tail_current)
        # print(tail_current)

    return result[:-1]


"""
def g2(n):
    result = []
    current_text = ""
    tail_current = [(0, 0)]
    two_way_pointer = []
    loop_index = 0
    add_left = True
    while True:
        current_len = len(current_text)
        if current_len == 2 * n:
            result.append(current_text)
            if not two_way_pointer:
                break
            back_index = two_way_pointer.pop()
            current_text = current_text[:back_index]
            tail_current = tail_current[: back_index + 1]
            tail_current.append((tail_current[back_index][0], tail_current[back_index][1] + 1))
        else:
            if add_left:
                two_way_pointer.append(current_len)
                current_text += "("
                tail_current.append((tail_current[current_len][0] + 1, tail_current[current_len][1]))
            else:
                current_text += ")"
                tail_current.append((tail_current[current_len][0], tail_current[current_len][1] + 1))
                add_left = True

        if tail_current[-1][0] > n:
            add_left = False
            if not two_way_pointer:
                break
            back_index = two_way_pointer.pop()
            current_text = current_text[:back_index]
            tail_current = tail_current[: back_index + 1]
            tail_current.append((tail_current[back_index][0], tail_current[back_index][1] + 1))
        elif tail_current[-1][1] > n:
            add_left = True
            if not two_way_pointer:
                break
            back_index = two_way_pointer.pop()
            current_text = current_text[:back_index]
            tail_current = tail_current[: back_index + 1]
            tail_current.append((tail_current[back_index][0], tail_current[back_index][1] + 1))

        if tail_current[1][1] == 1:
            if not two_way_pointer:
                break
            back_index = two_way_pointer.pop()
            current_text = current_text[:back_index]
            tail_current = tail_current[: back_index + 1]
            tail_current.append((tail_current[back_index][0], tail_current[back_index][1] + 1))
        print(result)

        loop_index += 1
    return result


def generateParenthesis(n):
    res = []

    def dfs(left, right, s):
        if len(s) == n * 2:
            res.append(s)
            return

        if left < n:
            dfs(left + 1, right, s + "(")

        if right < left:
            dfs(left, right, s + ")")

    dfs(0, 0, "")
    return res
"""

if __name__ == "__main__":
    x = 4
    result = generate_parentheses(x)
    # result = generateParenthesis(x)
    print(result)
    print(len(result))
