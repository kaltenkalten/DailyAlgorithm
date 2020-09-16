def get_unique_combination(arr):
  result = [[]]
  for i in arr:
    fix_result = result[:]
    for j in fix_result:
      result.append([i] + j)
  
  return result

cur_arr = list(range(len(relation[0])))

combination = get_unique_combination(cur_arr)
used = []
count = 0

for each in combination:
  str_arr = [''] * len(relation)
    
  if len(set(each) - set(used)) != len(each):
    continue
  for col in each:
    for row in range(len(relation)):
      str_arr[row] += relation[row][col]
    if len(set(str_arr)) == len(str_arr):
      count += 1
      used.extend(each)

print(count)

