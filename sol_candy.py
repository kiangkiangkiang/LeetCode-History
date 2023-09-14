def get_min_candy(ratings):
    diff = []
    change_sign = []
    for i in range(len(ratings) - 1):
        if ratings[i] > ratings[i + 1]:
            diff.append(-1)
        elif ratings[i] == ratings[i + 1]:
            diff.append(0)
        else:
            diff.append(1)

    for i, d in enumerate(diff):
        if i != 0:
            if d * prev_d < 0:
                change_sign.append(i)
            elif change_sign and d * prev_d == 0:
                change_sign.pop()
        prev_d = d

    result_pointer = 1
    result = [2] if diff[0] == -1 else [1]
    prev_d = None
    for i, d in enumerate(diff):
        if change_sign and i == change_sign[0]:
            while result[result_pointer - 1] + sum(diff[i:]) < 1:
                result[result_pointer - 1] += 1
            while result[result_pointer - 1] + sum(diff[i:]) > 1:
                result[result_pointer - 1] -= 1
            change_sign.pop(0)

        if d == 1:
            result.append(result[result_pointer - 1] + 1)
        elif d == -1:
            result.append(result[result_pointer - 1] - 1)
        else:
            min_candy = result[result_pointer - 1] - 1
            while min_candy + sum(diff[i:]) <= 0:
                min_candy += 1
            if prev_d == 0 and d == 0:
                result[result_pointer - 1] = 1
            result.append(min_candy)

        result_pointer += 1
        prev_d = d

    if result[-1] > result[-2]:
        return result
    else:
        result[-1] = 1
        return result


def get_min_candy2(ratings):
    diff = []
    change_sign = []
    for i in range(len(ratings) - 1):
        if ratings[i] > ratings[i + 1]:
            diff.append(-1)
        elif ratings[i] == ratings[i + 1]:
            diff.append(0)
        else:
            diff.append(1)
        if i != 0:
            if diff[i - 1] != diff[i]:
                change_sign.append(i)
    print(change_sign)

    result_pointer = 1
    result = [2] if diff[0] == -1 else [1]
    prev_d = None
    for i, d in enumerate(diff):
        if i != change_sign[i]:
            if d == 1:
                result.append(result[result_pointer - 1] + 1)
            elif d == -1:
                result.append(result[result_pointer - 1] - 1)
            else:
                result.append(1)
        else:
            if d == 1:
                min_candy = result[result_pointer - 1] + 1
            elif d == -1:
                min_candy = result[result_pointer - 1] - 1
        prev_d = d


if __name__ == "__main__":
    q = [1, 3, 2, 2, 1]  # 7
    # q = [29, 51, 87, 87, 87, 72, 12] # 13
    # q = [1, 2, 87, 87, 87, 87, 2, 1]  # 14
    # q = [1, 3, 4, 5, 2] # 11
    # q = [1, 6, 10, 8, 7, 3, 2]  # 18
    # q = [0, 1, 2, 3, 2, 1]  # 13
    a = get_min_candy2(q)
    print(a)
    # print(sum(a))
