def solution(play_time, adv_time, logs):
    answer = 0
    maxDuration = 0
    timeline = []
    
    def time2sec(time):
        h, m, s = time.split(':')
        return int(h) * 60 * 60 + int(m) * 60 + int(s)
    
    def sec2time(time):
        h = time // 3600
        m = (time % 3600) // 60
        s = time % 60
        return str(h)+":"+str(m)+":"+str(s)
    
    allTime = []
    for log in logs:
        start, end = log.split("-")
        start, end = time2sec(start), time2sec(end)
        allTime.append(start)
        allTime.append(end)
        
    timeline = list(set(allTime))
    timeline.sort()
    
    user = [0] * len(timeline)
    
    for log in logs:
        start, end = log.split("-")
        start, end = time2sec(start), time2sec(end)
        cnt = 0
        for idx, time in enumerate(timeline):
            if start < time:
                cnt = 1
            if end < time:
                cnt = 0
                break
            user[idx] += cnt
    adv_time = time2sec(adv_time)
    play_time = time2sec(play_time)
    print(timeline)
    print(user, adv_time)
    for startIdx, startTime in enumerate(timeline[:],0):
        tmpDuration = 0
        print('Start', startIdx, startTime)
        for endIdx, endTime in enumerate(timeline[startIdx:], startIdx):
            #print(endIdx, endTime, startTime)
            if play_time - startTime < adv_time:
                break
            if timeline[endIdx+1]-startTime > adv_time:
                #print(adv_time+startTime- endTime) 
                tmpDuration += (startTime+adv_time- timeline[endIdx]) * user[endIdx+1]
                print("Update", tmpDuration)
                break
            #if timeline[endIdx+1] > startTime + adv_time:
            #    tmpDuration += (startTime+adv_time - timeline[endIdx+1]) * user[endIdx]
            #   break
            print(startTime+adv_time, timeline[endIdx+1])
            #dur = timeline[endIdx+1] - timeline[endIdx]
            dur = timeline[endIdx+1] - timeline[endIdx]
            print(dur)
            tmpDuration += dur * user[endIdx+1]
        print("End", tmpDuration)     
        if tmpDuration > maxDuration:
            answer = startTime
            maxDuration = tmpDuration
            
            
    return sec2time(answer)
    
    
    
play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"] 

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))


