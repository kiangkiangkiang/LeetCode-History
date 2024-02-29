# 787. Cheapest Flights Within K Stops
# Medium
# Topics
# Companies
# There are n cities connected by some number of flights. You are given an array flights
# where flights[i] = [fromi, toi, pricei] indicates that
# there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k,
# return the cheapest price from src to dst with at most k stops.
#  If there is no such route, return -1.

# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

from collections import defaultdict
from copy import deepcopy
from typing import List


class Solution:
    def build_flight_tbl(self, flights):
        result = dict()
        track = defaultdict(list)
        for flight in flights:
            # result[[flight[0], flight[1]]] = flight[2]
            track[flight[0]].append(flight[1])
        track = sorted(track.items(), key=lambda x: x[0])
        return result, dict(track)

    def get_all_possible_transport_times(self, src, dst, transport_times, flight_price_tbl):
        # return [[[0, 1], [1, 3]], [[0, 2], [2, 3]]]
        pass

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_price_tbl, track_tbl = self.build_flight_tbl(flights)
        # go flight
        current_city = src
        current_ans = [src]
        final_result = []
        while track_tbl or current_ans:
            next_city = None
            # print(current_ans)
            if current_city in track_tbl:
                while track_tbl[current_city]:
                    next_city = track_tbl[current_city].pop()
                    if next_city not in current_ans:
                        current_ans.append(next_city)
                        break
                    next_city = None

                if not track_tbl[current_city]:
                    track_tbl.pop(current_city)

                if not next_city:
                    current_city = current_ans.pop()
            else:
                if current_ans:
                    next_city = current_ans.pop()
                else:
                    break

            if current_ans and current_ans[-1] == dst:
                final_result.append(current_ans[:])

            current_city = next_city
        return final_result
        # total_price = -1
        # for transport_times in range(k + 1):
        #     if transport_times == 0:
        #         if [src, dst] in flight_price_tbl:
        #             total_price = flight_price_tbl[[src, dst]]
        #         continue
        #     else:
        #         all_possible_transport_times = self.get_all_possible_transport_times(
        #             src=src, dst=dst, transport_times=transport_times, flight_price_tbl=flight_price_tbl
        #         )
        #         for possible_transport_times in all_possible_transport_times:
        #             tmp_total = sum([flight_price_tbl[transport] for transport in possible_transport_times])
        #             if tmp_total > total_price:
        #                 total_price = tmp_total
        # return total_price


from typing import List


class Solution:
    def build_flight_tbl(self, flights):
        track = defaultdict(list)
        for flight in flights:
            track[flight[0]].append(flight[1])
        track = sorted(track.items(), key=lambda x: x[0])
        return dict(track)

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        route_tbl = self.build_flight_tbl(flights)
        anser_list = []

        def helper(h_src, h_k, ans):
            if h_k < 0:
                return ans

            if h_src not in route_tbl:
                return

            for next_go in route_tbl[h_src]:
                helper(next_go, h_k - 1, ans + [next_go])

            # return [helper(next_go, h_k - 1, ans + [next_go]) for next_go in route_tbl[h_src]]

        return helper(src, k, ans=[src])


n = 4
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 2
a = Solution()
print(a.findCheapestPrice(n, flights, src, dst, k))
