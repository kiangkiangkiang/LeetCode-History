# You are given an integer array nums and a positive integer k.

# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

# A subarray is a contiguous sequence of elements within an array.


# Example 1:

# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
# Example 2:

# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        max_num_loc = [i for i, n in enumerate(nums) if n == max_num]
        max_windows_len = len(max_num_loc)
        if max_windows_len < k:
            return 0
        # sliding_windows = self.get_all_possible_sliding_windows(k, max_windows_len)
        total = 0
        n = len(nums)
        for window_len in range(k, max_windows_len + 1):
            pointer = 0
            while True:
                start = pointer
                end = pointer + window_len - 1
                if end >= max_windows_len:
                    break

                # pre drift
                pre_drift = 0
                if start == 0:
                    if max_num_loc[start] > 0:
                        pre_drift = max_num_loc[start]
                else:
                    pre_drift = max_num_loc[start] - max_num_loc[start - 1] - 1

                # post drift
                post_drift = 0
                if end == max_windows_len - 1:
                    if max_num_loc[end] < n - 1:
                        post_drift = n - 1 - max_num_loc[end]
                else:
                    post_drift = max_num_loc[end + 1] - max_num_loc[end] - 1

                if pre_drift > 0 and post_drift > 0:
                    total += 1 + pre_drift + post_drift + pre_drift * post_drift
                elif pre_drift:
                    total += 1 + pre_drift
                elif post_drift:
                    total += 1 + post_drift
                else:
                    total += 1

                pointer += 1

        return total


a = Solution()
nums = [3, 2, 3, 3]
nums = [1, 1, 3, 3, 2, 2, 2, 3]
k = 2
print(a.countSubarrays(nums, k))
