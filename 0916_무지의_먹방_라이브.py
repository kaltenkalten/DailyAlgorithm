def solution(food_times, k):

    def dfs(food_times, k):
        # print(food_times, k)
        if k < len(food_times):
            return k

        each_time = k // len(food_times)
        rest_time = k % len(food_times)
        tmp_food_times = []
        # print(rest_time, "rest_time")
        for idx, time in enumerate(food_times):
            tmp = time - each_time
            if tmp >= 0:
                food_times[idx] = tmp
            else:
                food_times[idx] = 0
                rest_time += -tmp

        if k == rest_time:
            return -1
        return dfs(food_times, rest_time)

    if sum(food_times) < k:
        return -1
    result = dfs(food_times, k)
    if result == -1:
        return -1
    # print(result)
    idx = 0
    # print(result+1)
    print(result, food_times)
    if sum(food_times) < result+1:  return -1
    
    for i in range(result+1):
        #print(i, idx)
        idx %= len(food_times)
        while food_times[idx] == 0:
            #print(idx)
            idx += 1
            idx %= len(food_times)
        #print(idx, i)
        food_times[idx] -= 1
        idx += 1
    return idx
food_times = [1, 3, 1, 1]
k = 5
print("Final : "+str(solution(food_times, k)))
food_times = [5, 5, 5]
k = 5
print("Final : "+str(solution(food_times, k)))
food_times = [3, 1, 2]
k = 5
print("Final : "+str(solution(food_times, k)))

