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
        current_text = (
            current_text[:back_index] + [")"] if tail_current[-1][1] <= tail_total else current_text[:back_index]
        )
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
            print(123)
            current_text, two_way_pointer, tail_current = drop_out_loop(current_text, two_way_pointer, tail_current)

        # print(current_text)
        # print(tail_current)
        print(result)
        print(tail_current)
        # print(tail_current)

    return result


if __name__ == "__main__":
    x = 3
    result = generate_parentheses(x)
    print(result)
    print(len(result))
