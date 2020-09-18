#whybeak suri
#n	weak	dist	result
#12	[1, 5, 6, 10]	[1, 2, 3, 4]	2
#12	[1, 3, 4, 9, 10]	[3, 5, 7]	1
# [4, 9, 10, 13, 16]

def solution(n, weak, dist):
  min_dist = float('inf')


  def bt(n, rest_weak, rest_dist):
    if len(rest_weak) == 0: return len(rest_dist)
    if len(rest_dist) == 0: return -1
    if len(rest_weak) == 1 and len(rest_dist) >= 1:
      return len(rest_dist)
    #print(rest_weak, rest_dist)
    for i in range(len(rest_weak)):
      if rest_weak[i] > rest_dist[0] + rest_weak[0]:
        break

    return bt(n, rest_weak[i:], rest_dist[1:])


  dist.sort(reverse=True)
  #weak + [val]
  len_weak = len(weak)
  for j in range(len_weak):
    tmp = bt(n, weak, dist)
    weak = weak[1:] + [weak[0] + n]
    
    if tmp != -1:
     min_dist = min(min_dist, len(dist) - tmp)
  
  return min_dist if min_dist != float('inf') else -1

n = 12	
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n, weak, dist))
