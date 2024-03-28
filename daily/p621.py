# You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n.
# Each cycle or interval allows the completion of one task.
# Tasks can be completed in any order, but there's a constraint: i
# dentical tasks must be separated by at least n intervals due to cooling time.

# ​Return the minimum number of intervals required to complete all tasks.


# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two cycles before doing A again.
# The same applies to task B. In the 3rd interval, neither A nor B can be done,
# so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

# Example 2:

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

from collections import Counter, deque

# With a cooling interval of 1, you can repeat a task after just one other task.
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        sorted_task = sorted(Counter(tasks).items(), key=lambda x: x[1])
        total_len = len(tasks) * n
        result = deque([None for i in range(total_len)])
        start = 0
        while sorted_task:
            current_letter, current_sum = sorted_task.pop()
            fill_area = list(range(start, total_len, n + 1))[:current_sum]

            fill_drift = 0
            while fill_area:
                this_fill = fill_area.pop(0)
                if fill_drift > 0:
                    this_fill += fill_drift
                while this_fill < total_len and result[this_fill]:
                    this_fill += 1
                    fill_drift += 1
                result[this_fill] = current_letter
            start += 1

        for i in reversed(range(total_len)):
            if not result[i]:
                result.pop()
            else:
                break

        return len(result)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        sorted_task = deque(
            sorted(list(Counter(tasks).items()), key=lambda x: x[1], reverse=True)
        )
        result = deque()
        pointer = 0
        print(123)
        while sorted_task:
            current = list(sorted_task.pop(pointer))

            result.append(current[0])
            current[1] -= 1
            if current[1] > 0:
                sorted_task.insert(pointer - 1, current)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        sorted_task = dict(
            sorted(list(Counter(tasks).items()), key=lambda x: x[1], reverse=True)
        )

        set_tasks = "".join([i for i in sorted_task.keys()])
        reduce_task = {}
        max_count = sorted_task[set_tasks[0]]
        for k, v in sorted_task.items():
            reduce_task[k] = max_count - v
        set_tasks = list(set_tasks * sorted_task[set_tasks[0]])
        pointer = len(set_tasks) - 1
        while pointer >= 0:
            if reduce_task[set_tasks[pointer]] > 0:
                reduce_task[set_tasks[pointer]] -= 1
                set_tasks.pop(pointer)

            pointer -= 1

        final_counter = 0
        index = 0
        final_dict = {}
        while set_tasks:
            this_char = set_tasks.pop(0)
            final_counter += 1
            if this_char in final_dict:
                last_index = final_dict[this_char]
                if index - last_index - 1 < n:
                    # add idle
                    final_counter = final_counter + (n + last_index + 1 - index)
                    index = n + last_index + 1
                    final_dict[this_char] = index
            else:
                final_dict[this_char] = index

            index += 1
        return final_counter


tasks = ["A", "A", "A", "B", "B", "B"]
n = 3
# tasks = ["A", "C", "A", "B", "D", "B"]
# n = 1
# tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
# n = 2
tasks = ["A", "A", "A", "B", "B", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
n = 7  # 18
a = Solution()
print(a.leastInterval(tasks=tasks, n=n))
