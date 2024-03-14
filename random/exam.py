def ArrayChallenge(arr):
    result = set()
    while arr:
        current = arr.pop()
        if current in result:
            return True
        if result:
            tmp = result.copy()
            for i in tmp:
                result.add(i + current)
        result.add(current)
        print(result)

    # code goes here
    return False


print(ArrayChallenge([5, 7, 16, 1, 2]))
