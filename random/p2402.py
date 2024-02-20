from typing import List


class Solution:
    def reset_current_index(self):
        pass

    def room_time_reset(self, time_consume):
        pass

    def time_going(self):
        time_reach = self.current_meetings[0]
        time_consume = time_reach - self.current_time
        self.room_time_reset(time_consume)

    def check_next_room_avaliable(self):
        next_meeting = self.meetings[0]
        if next_meeting[0] > self.current_time:
            time_consume = next_meeting[0] - self.current_time

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        self.meetings = meetings
        self.rooms = [[] * n]
        self.current_time = 0
        self.current_avaliable_index = 0
        while meetings:
            self.current_meetings = self.meetings.pop(0)
            self.rooms[self.current_avaliable_index] = self.current_meetings
            self.current_avaliable_index = self.check_next_room_avaliable()


class Solution:
    def reset_when_current_time_change(self):
        pass

    def time_going(self, time_consume):
        if time_consume == -1:
            # manually check all room
            pass
        else:
            self.current_time = self.meetings[0][0]

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        self.rooms = [[] * n]
        self.meetings = meetings
        self.current_time = 0
        while self.meetings:
            if self.meetings[0][0] > self.current_time:
                # not reach meeting time
                self.current_time = self.meetings[0][0]
                self.reset_when_current_time_change()
            else:
                if avaliable_room := self.check_room_avaliable() == -1:
                    self.time_going(time_consume=-1)
                else:
                    self.rooms[avaliable_room] = self.meetings.pop(0)

        # 1. check if reach meeting time
        # 2.1 if meeting time
        # 2.1.1 check if current room empty
        # 2.1.1.1 if not empty -> time going
        # 2.1.1.1 if empty -> asign

        # 2.2 if not meeting time -> time going


n = 3
meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
# ans: 1
a = Solution()
print(a.mostBooked())
