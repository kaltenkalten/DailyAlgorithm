class LL:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.starter = False

dic = {}
for i in range(ord('a'), ord('z')+1):
    dic[chr(i)] = LL(chr(i))

#print(dic)

connections = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt",
  "az",
  "au"
]


from collections import defaultdict

links = defaultdict(list)

for i in range(len(connections)-1):
    ch1 = connections[i][0]
    word1 = connections[i]
    ch2 = connections[i+1][0]
    word2 = connections[i+1]
    if ch1 != ch2:
        if dic[ch1].next is not None:
            tmp = dic[ch1].next
            dic[ch1].next = dic[ch2]
            dic[ch2].next = tmp
        else:
            dic[ch1].next = dic[ch2]
            if dic[ch1].starter is None: 
                dic[ch1].starter = True
        dic[ch2].starter = False
    else:
        idx = 0
        while idx < len(word1) and idx < len(word2):
            if word1[idx] != word2[idx]:
                ch1 = word1[idx]
                ch2 = word2[idx]
                if dic[ch1].next is not None:
                    tmp = dic[ch1].next
                    dic[ch1].next = dic[ch2]
                    dic[ch2].next = tmp
                else:
                    dic[ch1].next = dic[ch2]
                    if dic[ch1].starter is None: 
                        dic[ch1].starter = True
                dic[ch2].starter = False
                break
            idx += 1
            

for i in range(ord('a'), ord('z')+1):
    print(dic[chr(i)].starter, chr(i))

            
first_letter = connections[0][0]
cur = dic[first_letter]
while cur is not None:
    print(cur.val)
    cur = cur.next

dic[first_letter].starter = False
for i in range(ord('a'), ord('z')+1):
    if dic[chr(i)].starter:
        cur = dic[chr(i)]
        while cur is not None:
            print(cur.val)
            cur = cur.next        
        dic[chr(i)].starter = False
