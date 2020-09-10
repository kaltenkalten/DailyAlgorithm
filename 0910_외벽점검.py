def solution(n, weak, dist):
    global answer
    answer = float('inf')
    
    dist.sort(reverse=True)
    
    origin_weak_len = len(weak)
    for i in range(len(weak)):
        weak.append(weak[i]+n)
    
    def backtracking(rest_weak, dist, cnt):
        global answer
        if len(rest_weak) == 0:
            answer = min(answer, cnt)
            return
        if len(rest_weak) == 1 and len(dist) != 0:
            answer = min(answer, cnt)
            return
        if len(dist) == 0:
            return

        for i in range(len(rest_weak)):
            if rest_weak[i] > dist[0] + rest_weak[0]:
                break
        backtracking(rest_weak[i:], dist[1:], cnt+1)

    memo = {}
    for i in range(origin_weak_len):
        for j in range(i+1, origin_weak_len+i):
            if weak[j] > dist[0] + weak[i]:
                backtracking(weak[j:i+origin_weak_len], dist[1:], 1)
                break
    
    return answer if answer != float("inf") else -1
