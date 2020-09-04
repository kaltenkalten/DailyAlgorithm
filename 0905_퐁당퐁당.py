def solution(key, lock):
    # Step 2. (0, 0) ~ (3, 3) 돌면서 확인
    for i in range(4):
        for r in range(-len(key)+1, len(lock), 1):
            for c in range(-len(key[0])+1, len(lock[0]), 1):
                if check_lock(key, lock, r, c):
                    return True
        #rotation
        key = list(zip(*key))
        print(key)
    return False

def check_lock(key, lock, r, c):
    for lock_r in range(len(lock)):
        for lock_c in range(len(lock[0])):
            match = lock[lock_r][lock_c]
            #  r   lock_r
            # 0 -> 0,1,2   1 -> 0,1     2 -> 0 
            if 0 <= lock_r-r < len(key) and 0 <= lock_c-c < len(key[0]):
                match += key[lock_r-r][lock_c-c]
     Y
       
            if match != 1:
                return False

    return True
