yinput_str = 'GG'
cost_str = '0 0 100'
cost_str = cost_str.split(' ')
colors = ['R', 'G', 'B']
cost = {}
for i in range(3):
  cost[colors[i]] = int(cost_str[i])

size = len(input_str)
cases = []
cases.append(('RGB' * ((size // 3) + 1))[:size])
cases.append(('GBR' * ((size // 3) + 1))[:size])
cases.append(('BRG' * ((size // 3) + 1))[:size])

result = []

for case in cases:
  bucket = {'R':0, 'G':0, 'B':0, 'M':0}
  market = {'R':0, 'G':0, 'B':0}
  for i in range(size):
    if input_str[i] != case[i]:
      bucket[input_str[i]] += 1
      market[case[i]] += 1
      bucket['M'] += 1
  move = bucket['M']
  tmp_cost = 0
  for color in colors:
    tmp_cost += min(0, market[color] - bucket[color]) * cost[color]
  result.append((tmp_cost, move))    

result.sort()
print(result)
print(result[0])


