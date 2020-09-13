class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        timeline = []
        
        for s, e in intervals:
            timeline.append([s, 's'])
            timeline.append([e, 'e'])
        
        timeline.sort()
        
        s = e = 0
        
        occupied = 0
        vacant = 0
        
        for time, status in timeline:
            if status == 's':
                if vacant > 0:
                    vacant -= 1
                    occupied += 1
                else:
                    occupied += 1 
            if status == 'e':
                occupied -= 1
                vacant += 1
                
        return occupied + vacant
