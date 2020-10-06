
m queue import PriorityQueue
from collections import Counter
#tasks = ['A', 'A', 'A', 'A', 'B', 'B', 'C']
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
#tasks = ['A', 'A', 'A', 'B', 'B', 'B']
n = 2

idle = 0


d_c = Counter(tasks)
pq = PriorityQueue()
# A:3, B:2, C:1
for key, val in d_c.items():
    pq.put((val, key))


while pq.qsize() > 0:
    step = pq.qsize()
    tmp_arr = []
    for _ in range(step):
        val, key = pq.get()
        #print(key, val)
        if val > 1:
            tmp_arr.append((val-1, key))
    if len(tmp_arr) !=0 and step < n+1:
        #print('idle')
        idle += 1

    for tmp_k, tmp_v in tmp_arr:
        pq.put((tmp_k, tmp_v))

#print(idle)
print(len(tasks) + idle)
