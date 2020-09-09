class Trie:
  def __init__(self):
    self.children = {}
    self.count = 0

def solution(words, queries):
  answer = []

  # Split by Length
  d_len = {}
  for word in words:
    if len(word) in d_len:
      d_len[len(word)].append(word)
    else:
      d_len[len(word)] = [word]

  
  #print(d_len)
  
  # Build Trie
  d_trie = {}
  for key in d_len.keys():
    
    head = node = Trie()
    d_trie[key] = node

    for word in d_len[key]:
      node = head
      node.count += 1
      for ch in word:
        #print(node.children, ch)
        if ch in node.children:
          node.children[ch].count += 1
        else:
          new_node = Trie()
          new_node.count = 1
          node.children[ch] = new_node
        node = node.children[ch]

  #print(d_trie) 

  # Search Word in Trie
  for word in queries:
    if len(word) not in d_trie:
      answer.append(0)
      continue 
    node = d_trie[len(word)]
    #print(node.count) 
    for ch in word:
      #print(node.children, node.count)
      if ch == "?":
        answer.append(node.count)
        break
      if ch not in node.children:
        answer.append(0)
        break
      node = node.children[ch]
      
  return answer


  

#words queries result
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"] #[3, 2, 4, 1, 0]
#queries = ["fro??"] #[3, 2, 4, 1, 0]


print(solution(words, queries))
