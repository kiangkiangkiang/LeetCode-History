class Solution:
    def get_unit(self, _str, times):
        return _str * times

    # def get_combination(self, max_length, candidate_pool):
    #     stack = deque()
    #     current = deque()
    #     next_road = deque(candidate_pool[:])
    #     counter = 0
    #     len_controller = 0
    #     while next_road:
    #         if len_controller < max_length:
    #             _current = next_road.pop()
    #             len_controller += len(_current)
    #             current.append(_current)
    #             stack.append(next_road)
    #             next_road = candidate_pool[:]
    #         else:
    #             if len_controller == max_length:
    #                 counter += 1
    #             _current = current.pop()
    #             _next = stack.pop()
    #             len_controller -= len(_current)
    #             while len(_next) <= 0:
    #                 if not current:
    #                     break
    #                 _current = current.pop()
    #                 _next = stack.pop()
    #                 len_controller -= len(_current)

    #             next_road = _next
    #     return counter

    def count(self, x, y):
        def factorial(num):
            result = 1
            for i in range(1, num + 1):
                result *= i
            return result

        return int(factorial(x + y) / (factorial(x) * factorial(y)))

    def get_combination(self, max_length, zero_unit, one_unit):
        counter = 0
        for i in range(max_length + 1):
            for u in range(max_length + 1):
                total = i * zero_unit + u * one_unit
                if total == max_length:
                    if i == 0 or u == 0:
                        counter += 1
                    else:
                        tmp2 = self.count(i, u) % (10**9 + 7)
                        counter += tmp2
                        print(f"total, i, u, tmp2 = {total}, {i}, {u}, {tmp2}")
                elif total > max_length:
                    break
        return counter

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            ans = 1
            if i >= zero:
                ans += dp[i - zero]
            if i >= one:
                ans += dp[i - one]
            dp[i] = ans % mod
        return (dp[high] - dp[low - 1] + mod) % mod


a = Solution()
print(a.countGoodStrings(10, 10, 5, 2))
