def partition(arr, left, right):
    pivot = arr[left + (right -left) // 2]

    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left

def quicksort(arr, left, right):
    if left < right:
        #print(left, right)
        mid = partition(arr, left, right)
        #print(mid)
        quicksort(arr, left, mid-1)
        quicksort(arr, mid, right)



def merge(arr, left, mid, right):
    temp = []
    pointer_l = left
    pointer_r = mid + 1
    while pointer_l <= mid and pointer_r <= right:
        if arr[pointer_l] > arr[pointer_r]:
            temp.append(arr[pointer_r])
            pointer_r += 1
        else:
            temp.append(arr[pointer_l])
            pointer_l += 1

    while pointer_l <= mid:
        temp.append(arr[pointer_l])
        pointer_l += 1
    while pointer_r <= right:
        temp.append(arr[pointer_r])
        pointer_r += 1

    for i in range(len(temp)):
        arr[left+i] = temp[i]
    #print(temp)


def mergesort(arr, left, right):
    if right - left + 1 < 2:
        #print(arr[left:right + 1])
        return
    mid = left + (right-left)//2
    mergesort(arr, left, mid)
    mergesort(arr, mid+1, right)

    merge(arr, left, mid, right)



#arr = [3,4,1,2,5,7,3,8,9,0,-1,2,4,2,3,5,1,7,2,-2,40,-10]

#mergesort(arr, 0, len(arr)-1)
#quicksort(arr, 0, len(arr)-1)
print(arr)



