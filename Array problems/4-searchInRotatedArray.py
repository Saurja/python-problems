def findRotationSearchHelper(arr, low, high, key):
    if(high>low):
        return "No match!"

    mid = int(low + ((high - low) // 2))

    if arr[mid] == key:
        return mid

    if arr[low] <= arr[mid] and key <= arr[mid] and key >= arr[low]:
        return findRotationSearchHelper(arr, low, mid-1, key)
    elif arr[mid] <= arr[high] and key >= arr[mid] and key <= arr[high]:
        return findRotationSearchHelper(arr, mid+1, high, key)
    
    elif arr[high] <= arr[mid]:
        return findRotationSearchHelper(arr, mid+1, high, key)
    elif arr[low] >= arr[mid]:
        return findRotationSearchHelper(arr, low, mid-1, key)

    return -1

def findRotationSearch(arr, key):
    return (findRotationSearchHelper(arr, 0, len(arr)-1, key))

arr = (4, 5, 6, 1, 2, 3)
index = findRotationSearch(arr, 2)
print("Value is at index : {}".format(index))