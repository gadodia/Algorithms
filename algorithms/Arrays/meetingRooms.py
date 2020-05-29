'''
This problem was recently asked by Facebook:

Given a list of meetings that will happen during a day, find the minimum number of meeting rooms that can fit all meetings.

Each meeting will be represented by a tuple of (start_time, end_time), where both start_time and end_time will be represented by an integer to indicate the time. start_time will be inclusive, and end_time will be exclusive, meaning a meeting of (0, 10) and (10, 20) will only require 1 meeting room.

'''

class Solution:

    def meeting_rooms(self, meetings):
        rooms = 0
        available = 0
        starttimes = []
        endtimes = []
        i = 0
        j = 0
        for start, end in meetings:
            starttimes.append(start)
            endtimes.append(end)
        starttimes.sort()
        endtimes.sort()
        while i < len(meetings):
            if starttimes[i] < endtimes[j]:
                if available:
                    available -= 1
                else:
                    rooms += 1
                i += 1
            elif endtimes[j] > starttimes[i]:
                available += 1
                j += 1
            else:
                i += 1
                j += 1
        return rooms



print(Solution().meeting_rooms([(0, 10), (10, 20)]))
# 1

print(Solution().meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# 3 (all meetings overlap at time 20)
