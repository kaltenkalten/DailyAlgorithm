class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        answer = []
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            #print(sorted_s)
            if sorted_s in d:
                idx = d[sorted_s]
                answer[idx].append(s)
            else:
                d[sorted_s] = len(d)
                answer.append([s])
                
        return answer
        # from collections import Counter
        
        # Takes too long
#         arr = []
#         answer = []
        
#         for s in strs:
#             counter_s = Counter(s)
#             flag = False
#             for idx, value in enumerate(arr):
#                 if counter_s == value:
#                     answer[idx].append(s)
#                     flag = True
#                     break
#             if not flag:
#                 answer.append([s])
#                 arr.append(counter_s)
        
#         return answer
