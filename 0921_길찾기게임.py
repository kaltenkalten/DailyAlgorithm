class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def bt(rest_arr, d_x):
    if len(rest_arr) == 0:  return None

    parents_x, parents_y = rest_arr[0]
    node = Tree(d_x[parents_x])
    left_arr = []
    right_arr = []
    for nearest_level in rest_arr[1:]:
        if nearest_level[1] > parents_y:
            break

    for tmp_x, tmp_y in rest_arr[1:]:
    # print(tmp_x, tmp_y, nearest_level[1])
        if tmp_y == nearest_level[1] or nearest_level[1] < tmp_y:
            if tmp_x <  parents_x:
                left_arr.append([tmp_x, tmp_y])
            elif tmp_x > parents_x:
                right_arr.append([tmp_x, tmp_y])
    node.left = bt(left_arr, d_x)
    node.right = bt(right_arr, d_x)

    return node


def solution(nodeinfo):
    if len(nodeinfo) == 0:  return [[],[]]
    
    d_x = {val[0]:idx+1 for idx,val in enumerate(nodeinfo)}
    nodeinfo.sort(key=lambda x:x[1], reverse=True)
    node = bt(nodeinfo, d_x)
    
    result = [[],[]]
    def post_order(node, result):
        if node is None:  return

        post_order(node.left, result)
        post_order(node.right, result)
        #print(node.val)
        result[0].append(node.val)

    def pre_order(node, result):
        if node is None:  return

        result[1].append(node.val)
        #print(node.val)
        pre_order(node.left, result)
        pre_order(node.right, result)

    def inorder(node):
        if node is None:    return
        
        inorder(node.left)
        #print(node.val)
        inorder(node.right)
    
    #inorder(node)
    post_order(node, result)
    pre_order(node, result)
    #print(result)
    result = [result[1], result[0]]
    return result
    

