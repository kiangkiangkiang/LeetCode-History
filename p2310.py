class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        possible_set = [k]
        possible_dict = {k: ""}
        total = 0
        if num == 0:
            return 0
        else:
            while possible_set[-1] <= num:
                possible_set.append(possible_set[-1] + 10)
                possible_dict.update({possible_set[-1]: ""})
            if possible_set[-1] > num:
                possible_dict.pop(possible_set[-1])
                possible_set.pop()

        for i in possible_dict:
            # print("i: ", i)
            possible_dict[i] = 1
            remain = num - i
            if remain == 0:
                total += 1
                continue

            if i == remain:
                continue

            if remain in possible_dict and possible_dict[remain] != 1:
                possible_dict[remain] = 1
                total += 1

        return total if total > 0 else -1


s = Solution()
ans = s.minimumNumbers(num=1, k=1)
print(ans)
